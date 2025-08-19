#!/usr/bin/env python3
"""
Extract detailed authentication-related issues from Azure Dev CLI GitHub repository data.
Creates a comprehensive report similar to the environment issues detailed report.
"""

import json
import os
import re
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import argparse


def is_auth_related(issue):
    """
    Determine if an issue is authentication-related based on title, labels, and content.
    """
    auth_keywords = [
        'auth', 'login', 'credential', 'token', 'authentication', 'authenticate',
        'oauth', 'saml', 'federation', 'federated', 'sso', 'single sign',
        'service principal', 'sp', 'identity', 'tenant', 'multi-tenant',
        'device code', 'browser', 'interactive', 'non-interactive',
        'azd login', 'azd auth', 'auth login', 'logged in', 'sign in', 'signin',
        'refresh token', 'access token', 'bearer token', 'jwt',
        'permission', 'unauthorized', 'forbidden', 'invalid credentials',
        'client secret', 'client id', 'app registration', 'azure ad', 'entra',
        'msal', 'adal', 'azure cli', 'az login', 'certificate',
        'keychain', 'credential store', 'cache', 'session',
        'wsl', 'cloud shell', 'codespace', 'container auth'
    ]
    
    # Auth-related labels
    auth_labels = ['authn', 'auth', 'authentication', 'login', 'credential']
    
    title = issue.get('title', '').lower()
    body = issue.get('body', '').lower() if issue.get('body') else ''
    labels = [label.get('name', '').lower() for label in issue.get('labels', [])]
    
    # Check title for auth keywords
    for keyword in auth_keywords:
        if keyword in title:
            return True
    
    # Check labels
    for label in labels:
        if any(auth_label in label for auth_label in auth_labels):
            return True
    
    # Check body for auth keywords (less strict to avoid false positives)
    critical_auth_terms = [
        'azd login', 'azd auth', 'auth login', 'authentication', 'login',
        'credential', 'service principal', 'federated', 'oauth', 'saml'
    ]
    
    for term in critical_auth_terms:
        if term in body:
            return True
    
    return False


def categorize_auth_issue(issue):
    """
    Categorize authentication issues into specific subtypes.
    """
    title = issue.get('title', '').lower()
    body = issue.get('body', '').lower() if issue.get('body') else ''
    labels = [label.get('name', '').lower() for label in issue.get('labels', [])]
    
    text = f"{title} {body}".lower()
    
    categories = []
    
    # Platform-specific issues
    if any(term in text for term in ['wsl', 'windows subsystem', 'ubuntu', 'linux']):
        categories.append('WSL/Linux')
    elif any(term in text for term in ['windows', 'powershell', 'cmd']):
        categories.append('Windows')
    elif any(term in text for term in ['macos', 'mac', 'darwin']):
        categories.append('macOS')
    
    # Environment-specific
    if any(term in text for term in ['cloud shell', 'cloudshell', 'azure cloud shell']):
        categories.append('Cloud Shell')
    elif any(term in text for term in ['docker', 'container', 'containerized']):
        categories.append('Container')
    elif any(term in text for term in ['codespace', 'github codespace']):
        categories.append('Codespaces')
    elif any(term in text for term in ['ci/cd', 'github action', 'pipeline', 'jenkins', 'devops']):
        categories.append('CI/CD')
    
    # Auth method specific
    if any(term in text for term in ['device code', 'device-code', '--use-device-code']):
        categories.append('Device Code Flow')
    elif any(term in text for term in ['service principal', 'sp', 'client secret', 'client credential']):
        categories.append('Service Principal')
    elif any(term in text for term in ['federated', 'federation', 'federated credential']):
        categories.append('Federated Identity')
    elif any(term in text for term in ['interactive', 'browser', 'popup', 'redirect']):
        categories.append('Interactive Auth')
    elif any(term in text for term in ['certificate', 'cert', 'x509']):
        categories.append('Certificate Auth')
    
    # Specific issues
    if any(term in text for term in ['token', 'refresh', 'expired', 'expir']):
        categories.append('Token Management')
    elif any(term in text for term in ['multi-tenant', 'tenant', 'cross-tenant']):
        categories.append('Multi-tenant')
    elif any(term in text for term in ['permission', 'unauthorized', 'forbidden', '403', '401']):
        categories.append('Permissions')
    elif any(term in text for term in ['cache', 'credential store', 'keychain', 'stored']):
        categories.append('Credential Storage')
    
    return categories if categories else ['General Auth']


def calculate_priority_score(issue):
    """
    Calculate a priority score for authentication issues.
    """
    score = 0
    
    # Base score from reactions
    reactions = issue.get('reactions', {})
    score += reactions.get('total_count', 0) * 2
    
    # Comments indicate engagement
    score += min(issue.get('comments', 0), 20)  # Cap at 20 to avoid skewing
    
    # Labels that indicate severity
    labels = [label.get('name', '').lower() for label in issue.get('labels', [])]
    
    if any(label in ['bug', 'critical', 'high-priority'] for label in labels):
        score += 10
    if any(label in ['customer-reported', 'escalation'] for label in labels):
        score += 8
    if any(label in ['needs-team-attention', 'blocking'] for label in labels):
        score += 6
    if any(label in ['enhancement', 'feature-request'] for label in labels):
        score += 3
    
    # Recent activity
    updated = issue.get('updated_at', '')
    if updated:
        try:
            update_date = datetime.fromisoformat(updated.replace('Z', '+00:00'))
            days_since_update = (datetime.now().astimezone() - update_date).days
            if days_since_update < 30:
                score += 5
            elif days_since_update < 90:
                score += 2
        except:
            pass
    
    return score


def generate_detailed_auth_report(data_files, output_file):
    """
    Generate a comprehensive authentication issues report.
    """
    all_auth_issues = []
    processed_issues = set()
    
    # Process all data files
    for file_path in data_files:
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            continue
            
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle different data structures
            issues_data = []
            if isinstance(data, list):
                issues_data = data
            elif isinstance(data, dict):
                if 'issues' in data:
                    issues_data = data['issues']
                elif 'data' in data:
                    issues_data = data['data']
                else:
                    # Try to find any list of issues
                    for key, value in data.items():
                        if isinstance(value, list) and value and 'number' in str(value[0]):
                            issues_data = value
                            break
            
            # Process issues
            for issue in issues_data:
                if not isinstance(issue, dict):
                    continue
                    
                issue_number = issue.get('number')
                if not issue_number or issue_number in processed_issues:
                    continue
                
                if is_auth_related(issue):
                    processed_issues.add(issue_number)
                    
                    # Add calculated fields
                    issue['categories'] = categorize_auth_issue(issue)
                    issue['priority_score'] = calculate_priority_score(issue)
                    
                    all_auth_issues.append(issue)
                    
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    print(f"Found {len(all_auth_issues)} authentication-related issues")
    
    # Sort by priority score (descending) and then by issue number
    all_auth_issues.sort(key=lambda x: (-x['priority_score'], -x.get('number', 0)))
    
    # Generate report
    generate_report(all_auth_issues, output_file)


def generate_report(auth_issues, output_file):
    """
    Generate the detailed authentication issues report.
    """
    now = datetime.now()
    
    # Filter to open issues only and calculate statistics
    open_issues = [issue for issue in auth_issues if issue.get('state') == 'open']
    total_issues = len(open_issues)
    
    # Category analysis (open issues only)
    category_stats = defaultdict(int)
    platform_stats = defaultdict(int)
    priority_distribution = {'high': 0, 'medium': 0, 'low': 0}
    
    for issue in open_issues:
        categories = issue.get('categories', ['General Auth'])
        for cat in categories:
            category_stats[cat] += 1
        
        # Platform classification
        if any(cat in ['WSL/Linux', 'Windows', 'macOS'] for cat in categories):
            for cat in categories:
                if cat in ['WSL/Linux', 'Windows', 'macOS']:
                    platform_stats[cat] += 1
        else:
            platform_stats['Cross-platform'] += 1
        
        # Priority classification
        score = issue.get('priority_score', 0)
        if score > 20:
            priority_distribution['high'] += 1
        elif score > 10:
            priority_distribution['medium'] += 1
        else:
            priority_distribution['low'] += 1
    
    # Most active issues (by comments and reactions) - open issues only
    most_active = sorted(open_issues, 
                        key=lambda x: (x.get('comments', 0) + x.get('reactions', {}).get('total_count', 0)), 
                        reverse=True)[:10]
    
    # Recent issues (last 90 days) - open issues only
    recent_cutoff = datetime.now().replace(tzinfo=None) - timedelta(days=90)
    recent_issues = []
    for issue in open_issues:
        created_at = issue.get('created_at', '')
        if created_at:
            try:
                created_date = datetime.fromisoformat(created_at.replace('Z', ''))
                if created_date >= recent_cutoff:
                    recent_issues.append(issue)
            except:
                pass
    
    # Generate markdown report
    report_content = f"""# Azure Developer CLI (azd) - Open Authentication Issues Detailed Analysis

**Generated:** {now.strftime('%B %d, %Y')}  
**Repository:** Azure/azure-dev  
**Focus:** Open Authentication, Login, and Credential Management Issues  
**Total Open Authentication Issues Analyzed:** {total_issues}

## Executive Summary

This report provides a comprehensive analysis of open authentication-related issues in the Azure Developer CLI repository. Open authentication problems represent a significant portion of actionable issues in the repository.

### Key Metrics

- **Total Open Authentication Issues:** {total_issues}
- **Average Priority Score:** {sum(issue.get('priority_score', 0) for issue in open_issues) / len(open_issues):.1f}

### Top Issue Categories

"""
    
    # Add category breakdown
    sorted_categories = sorted(category_stats.items(), key=lambda x: x[1], reverse=True)
    for i, (category, count) in enumerate(sorted_categories[:10], 1):
        percentage = (count / total_issues) * 100
        report_content += f"{i}. **{category}:** {count} issues ({percentage:.1f}%)\n"
    
    report_content += f"""

### Platform Distribution

"""
    
    for platform, count in sorted(platform_stats.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_issues) * 100
        report_content += f"- **{platform}:** {count} issues ({percentage:.1f}%)\n"
    
    report_content += f"""

### Priority Distribution

- **High Priority (Score > 20):** {priority_distribution['high']} issues
- **Medium Priority (Score 10-20):** {priority_distribution['medium']} issues  
- **Low Priority (Score < 10):** {priority_distribution['low']} issues

## Detailed Issue Analysis

### Most Critical Authentication Issues (Top 20 by Priority Score)

| Issue | Title | Created | Days Open | Comments | Priority Score | Categories |
|-------|-------|---------|-----------|----------|---------------|------------|
"""
    
    # Add top 20 critical issues (open only)
    for issue in sorted(open_issues, key=lambda x: -x.get('priority_score', 0))[:20]:
        number = issue.get('number', 'N/A')
        title = issue.get('title', 'No title')[:80]
        if len(issue.get('title', '')) > 80:
            title += '...'
        
        created = issue.get('created_at', '')
        if created:
            try:
                created_date = datetime.fromisoformat(created.replace('Z', ''))
                days_open = (datetime.now().replace(tzinfo=None) - created_date).days
            except:
                days_open = 'N/A'
        else:
            days_open = 'N/A'
        
        comments = issue.get('comments', 0)
        priority = issue.get('priority_score', 0)
        categories = ', '.join(issue.get('categories', ['General Auth']))
        
        report_content += f"| {number} | [{title}](https://github.com/Azure/azure-dev/issues/{number}) | {created[:10] if created else 'N/A'} | {days_open} | {comments} | {priority} | {categories} |\n"
    
    report_content += f"""

### Most Active Authentication Issues (by Community Engagement)

| Issue | Title | Comments | Reactions | Priority Score |
|-------|-------|----------|-----------|---------------|
"""
    
    # Add most active issues
    for issue in most_active[:10]:
        number = issue.get('number', 'N/A')
        title = issue.get('title', 'No title')[:60]
        if len(issue.get('title', '')) > 60:
            title += '...'
        
        comments = issue.get('comments', 0)
        reactions = issue.get('reactions', {}).get('total_count', 0)
        priority = issue.get('priority_score', 0)
        
        report_content += f"| {number} | [{title}](https://github.com/Azure/azure-dev/issues/{number}) | {comments} | {reactions} | {priority} |\n"
    
    report_content += f"""

### Recent Authentication Issues (Last 90 Days)

| Issue | Title | Created | Priority Score | Categories |
|-------|-------|---------|---------------|------------|
"""
    
    # Add recent issues
    for issue in sorted(recent_issues, key=lambda x: x.get('created_at', ''), reverse=True)[:15]:
        number = issue.get('number', 'N/A')
        title = issue.get('title', 'No title')[:70]
        if len(issue.get('title', '')) > 70:
            title += '...'
        
        created = issue.get('created_at', '')[:10] if issue.get('created_at') else 'N/A'
        priority = issue.get('priority_score', 0)
        categories = ', '.join(issue.get('categories', ['General Auth'])[:2])  # Limit categories for table width
        
        report_content += f"| {number} | [{title}](https://github.com/Azure/azure-dev/issues/{number}) | {created} | {priority} | {categories} |\n"
    
    report_content += f"""

## Category Deep Dive

### WSL/Linux Authentication Issues

WSL (Windows Subsystem for Linux) authentication represents one of the most challenging areas, with unique issues around:
- Browser integration and display forwarding
- Credential storage and keychain integration  
- Token persistence across WSL sessions
- SSH key management and forwarding

### Service Principal Authentication

Service principal authentication issues commonly involve:
- Configuration complexity and documentation gaps
- Certificate vs. secret-based authentication
- Multi-tenant scenarios and cross-tenant access
- CI/CD pipeline integration challenges

### Device Code Flow Issues

Device code authentication problems include:
- Browser availability in containerized environments
- Network restrictions and proxy configurations
- User experience friction in automated scenarios
- Token expiration and refresh handling

## Recommendations

### Immediate Actions (Next 30 Days)

1. **WSL Authentication Sprint:** Focus on top 10 WSL-related authentication issues
2. **Service Principal Documentation:** Create comprehensive SP setup guides
3. **Error Message Improvement:** Implement detailed error messages with troubleshooting steps
4. **Authentication Health Check:** Add `azd auth status --detailed` command

### Medium-term Goals (Next 90 Days)

1. **Unified Auth Flow:** Implement consistent authentication across all platforms
2. **Credential Management:** Improve token storage and refresh mechanisms
3. **CI/CD Integration:** Streamline authentication for automated scenarios
4. **Multi-tenant Support:** Enhance cross-tenant authentication capabilities

### Long-term Vision (Next 6 Months)

1. **Authentication SDK:** Create reusable authentication components
2. **Advanced Diagnostics:** Implement comprehensive auth troubleshooting tools
3. **Zero-config Auth:** Work toward seamless authentication experiences
4. **Enterprise Features:** Add advanced enterprise authentication features

## Appendix

### All Authentication Issues by Category

"""
    
    # Add full categorized listing
    for category, count in sorted_categories:
        if count == 0:
            continue
            
        report_content += f"\n#### {category} ({count} issues)\n\n"
        category_issues = [issue for issue in open_issues if category in issue.get('categories', [])]
        category_issues.sort(key=lambda x: -x.get('priority_score', 0))
        
        for issue in category_issues[:10]:  # Limit to top 10 per category
            number = issue.get('number', 'N/A')
            title = issue.get('title', 'No title')
            state = issue.get('state', 'unknown')
            comments = issue.get('comments', 0)
            
            report_content += f"- [#{number}](https://github.com/Azure/azure-dev/issues/{number}) {title} ({comments} comments)\n"
        
        if len(category_issues) > 10:
            report_content += f"- ... and {len(category_issues) - 10} more issues\n"
    
    report_content += f"""

---

**Report Generation Details:**
- **Generated on:** {now.strftime('%Y-%m-%d %H:%M:%S')}
- **Data sources:** GitHub Issues API data from azure-dev repository
- **Analysis method:** Automated categorization and priority scoring
- **Issue identification:** Keyword-based matching for authentication-related content

*This report is automatically generated from GitHub Issues data and provides insights into authentication-related challenges in the Azure Developer CLI project.*
"""
    
    # Write report to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"Open authentication issues detailed report generated: {output_file}")
    print(f"Total open authentication issues: {total_issues}")
    print(f"Categories found: {len(category_stats)}")


def main():
    parser = argparse.ArgumentParser(description='Extract detailed authentication issues from Azure Dev CLI data')
    parser.add_argument('--data-dir', default='tools/data/raw-data', 
                       help='Directory containing JSON data files')
    parser.add_argument('--output', default='reports/authentication-issues-detailed.md',
                       help='Output file path')
    parser.add_argument('--files', nargs='*', 
                       help='Specific data files to process (optional)')
    
    args = parser.parse_args()
    
    # Determine data files to process
    if args.files:
        data_files = args.files
    else:
        data_dir = args.data_dir
        data_files = []
        
        if os.path.exists(data_dir):
            for filename in os.listdir(data_dir):
                if filename.endswith('.json'):
                    data_files.append(os.path.join(data_dir, filename))
        
        if not data_files:
            print(f"No JSON files found in {data_dir}")
            return
    
    # Generate report
    print("Starting authentication issues extraction...")
    generate_detailed_auth_report(data_files, args.output)
    print("Authentication issues analysis complete!")


if __name__ == '__main__':
    main()
