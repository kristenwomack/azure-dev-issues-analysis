#!/usr/bin/env python3
"""
Authentication Issues Extractor
Fetches all authentication-related issues from Azure/azure-dev and creates a detailed report
"""

import requests
import json
import os
from datetime import datetime, timedelta
import time

def get_all_auth_issues():
    """Fetch all authentication-related issues from Azure/azure-dev"""
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ GITHUB_TOKEN environment variable not found")
        return []
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    base_url = 'https://api.github.com'
    repo_owner = 'Azure'
    repo_name = 'azure-dev'
    
    all_issues = []
    auth_issues = []
    page = 1
    
    print("🔍 Fetching all issues to identify authentication-related ones...")
    
    while True:
        url = f"{base_url}/repos/{repo_owner}/{repo_name}/issues"
        params = {
            'state': 'all',  # Get both open and closed
            'per_page': 100,
            'page': page,
            'sort': 'created',
            'direction': 'desc'
        }
        
        print(f"   📄 Fetching page {page}...")
        
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                print(f"❌ API Error: {response.status_code}")
                break
                
            issues = response.json()
            
            if not issues:
                print(f"   ✅ Completed - no more issues on page {page}")
                break
                
            all_issues.extend(issues)
            print(f"   📊 Found {len(issues)} issues on page {page}")
            
            # Rate limiting
            time.sleep(0.5)
            page += 1
            
        except Exception as e:
            print(f"❌ Error fetching issues: {e}")
            break
    
    print(f"\n📈 Total issues fetched: {len(all_issues)}")
    
    # Authentication keywords to search for
    auth_keywords = [
        'auth', 'authentication', 'login', 'logout', 'signin', 'sign-in',
        'token', 'credential', 'oauth', 'saml', 'sso', 'identity',
        'tenant', 'principal', 'service principal', 'managed identity',
        'browser', 'device code', 'interactive', 'federated',
        'azd login', 'azd auth', 'az login', 'unauthorized', '401',
        'permission', 'access denied', 'forbidden', '403'
    ]
    
    print(f"🔍 Searching for authentication-related issues...")
    
    for issue in all_issues:
        title_lower = issue['title'].lower()
        body_lower = (issue['body'] or '').lower()
        
        # Check for authentication keywords in title or body
        is_auth_issue = False
        matched_keywords = []
        
        for keyword in auth_keywords:
            if keyword in title_lower or keyword in body_lower:
                is_auth_issue = True
                matched_keywords.append(keyword)
        
        if is_auth_issue:
            issue['matched_keywords'] = list(set(matched_keywords))
            auth_issues.append(issue)
    
    print(f"📊 Found {len(auth_issues)} authentication-related issues out of {len(all_issues)} total")
    
    return auth_issues

def calculate_age_in_days(created_at):
    """Calculate age of issue in days"""
    created = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
    now = datetime.now(created.tzinfo)
    return (now - created).days

def generate_auth_report(auth_issues):
    """Generate detailed authentication issues report - open issues only"""
    
    # Filter to only open issues
    open_issues = [issue for issue in auth_issues if issue['state'] == 'open']
    
    # Calculate average age of open issues
    total_age = sum(calculate_age_in_days(issue['created_at']) for issue in open_issues)
    avg_age = total_age / len(open_issues) if open_issues else 0
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d")
    
    report_content = f"""# Authentication Issues - Azure Developer CLI

**Report Generated:** {datetime.now().strftime("%B %d, %Y")}  
**Repository:** Azure/azure-dev  
**Total Authentication Issues:** {len(open_issues)}  
**Data Source:** GitHub Issues API

## Summary

This report contains open authentication and login related issues from the Azure Developer CLI repository. Issues are identified by keywords related to authentication, login, credentials, tokens, and access management.

**Quick Stats:**
- **Open Issues**: {len(open_issues)}
- **Average Age**: {avg_age:.0f} days

## 🔴 Open Authentication Issues

| # | Issue Title | Created | Age (Days) | Comments | Labels |
|---|-------------|---------|------------|----------|--------|
"""

    # Add open issues table
    for issue in sorted(open_issues, key=lambda x: x['number'], reverse=True):
        age = calculate_age_in_days(issue['created_at'])
        created_date = datetime.fromisoformat(issue['created_at'].replace('Z', '+00:00')).strftime("%Y-%m-%d")
        labels = ', '.join([label['name'] for label in issue['labels']]) if issue['labels'] else ''
        
        report_content += f"| {issue['number']} | [{issue['title']}]({issue['html_url']}) | {created_date} | {age} | {issue['comments']} | {labels} |\n"

    # Add analysis section
    report_content += f"""

## 📊 Analysis

### Issue Categories

Based on keyword analysis, authentication issues fall into these categories:

"""

    # Analyze keywords from open issues only
    keyword_counts = {}
    for issue in open_issues:
        for keyword in issue.get('matched_keywords', []):
            keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1

    # Sort by frequency
    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

    for keyword, count in sorted_keywords[:15]:  # Top 15 keywords
        percentage = (count / len(open_issues)) * 100 if open_issues else 0
        report_content += f"- **{keyword}**: {count} issues ({percentage:.1f}%)\n"

    # Add top issues by comments (open issues only)
    report_content += f"""

### Most Discussed Open Authentication Issues

These are the open authentication issues with the most community engagement:

"""

    # Sort by comments - open issues only
    top_commented = sorted(open_issues, key=lambda x: x['comments'], reverse=True)[:10]
    
    for issue in top_commented:
        if issue['comments'] > 0:
            age = calculate_age_in_days(issue['created_at'])
            report_content += f"- **[#{issue['number']}]({issue['html_url']})** - {issue['title']} ({issue['comments']} comments, {age} days old)\n"

    # Add recent activity
    report_content += f"""

### Recent Open Authentication Issues (Last 30 Days)

"""

    # Filter recent issues (open only)
    from datetime import timezone
    thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)
    recent_issues = [
        issue for issue in open_issues 
        if datetime.fromisoformat(issue['created_at'].replace('Z', '+00:00')) > thirty_days_ago
    ]

    if recent_issues:
        for issue in sorted(recent_issues, key=lambda x: x['created_at'], reverse=True):
            age = calculate_age_in_days(issue['created_at'])
            report_content += f"- **[#{issue['number']}]({issue['html_url']})** - {issue['title']} ({age} days ago)\n"
    else:
        report_content += "No open authentication issues created in the last 30 days.\n"

    # Add platform analysis
    report_content += f"""

### Platform-Specific Analysis

Authentication issues by platform and environment:

"""

    # Analyze platform mentions
    platforms = {
        'Windows': ['windows', 'win32', 'powershell', 'cmd'],
        'macOS': ['macos', 'mac', 'darwin', 'brew'],
        'Linux': ['linux', 'ubuntu', 'debian', 'centos'],
        'GitHub Actions': ['github actions', 'gh actions', 'ci/cd', 'workflow'],
        'Azure DevOps': ['azure devops', 'ado', 'azdo'],
        'Docker': ['docker', 'container', 'containerized'],
        'Cloud Shell': ['cloud shell', 'cloudshell'],
        'VS Code': ['vscode', 'vs code', 'extension'],
        'WSL': ['wsl', 'windows subsystem']
    }

    platform_counts = {platform: 0 for platform in platforms.keys()}
    
    for issue in open_issues:
        issue_text = f"{issue['title']} {issue['body'] or ''}".lower()
        for platform, keywords in platforms.items():
            if any(keyword in issue_text for keyword in keywords):
                platform_counts[platform] += 1

    for platform, count in sorted(platform_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            percentage = (count / len(open_issues)) * 100 if open_issues else 0
            report_content += f"- **{platform}**: {count} issues ({percentage:.1f}%)\n"

    # Add recommendations
    report_content += f"""

## 🎯 Recommendations

Based on the analysis of {len(open_issues)} open authentication-related issues:

### Top Priority Areas

1. **Cross-Platform Authentication Consistency**
   - Standardize authentication flows across Windows, macOS, and Linux
   - Address platform-specific authentication challenges

2. **CI/CD Integration Improvements**
   - Better service principal and managed identity support
   - Improved token management for automated workflows

3. **Error Messaging Enhancement**
   - More descriptive authentication error messages
   - Better troubleshooting guidance for common auth failures

4. **Documentation and Guidance**
   - Comprehensive authentication troubleshooting guide
   - Platform-specific authentication setup instructions

5. **Browser and Device Code Flow Reliability**
   - Improved handling of browser-based authentication
   - Better fallback mechanisms for headless environments

### Suggested Features

- `azd auth status --detailed` command for diagnostics
- `azd auth reset` command for clearing corrupted auth state
- Better integration with Azure CLI authentication
- Support for custom authentication endpoints

---

*This report was generated on {datetime.now().strftime("%B %d, %Y")} using the Azure Developer CLI Issues Analysis Framework.*
"""

    return report_content

def main():
    print("🚀 Azure Developer CLI - Authentication Issues Analysis")
    print("=" * 60)
    
    # Fetch authentication issues
    auth_issues = get_all_auth_issues()
    
    if not auth_issues:
        print("❌ No authentication issues found or error occurred")
        return
    
    # Generate report
    print("\n📝 Generating detailed authentication issues report...")
    report_content = generate_auth_report(auth_issues)
    
    # Save report
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"../reports/auth-issues-detailed-{timestamp}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"✅ Report saved to: {filename}")
    print(f"📊 Total authentication issues analyzed: {len(auth_issues)}")
    
    # Save raw data as JSON
    json_filename = f"data/raw-data/auth_issues_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(auth_issues, f, indent=2)
    
    print(f"💾 Raw data saved to: {json_filename}")

if __name__ == "__main__":
    main()
