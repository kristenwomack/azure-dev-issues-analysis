#!/usr/bin/env python3
"""
Extract ALL authentication-related issues from Azure Dev CLI GitHub repository data.
Creates a comprehensive report with complete listings instead of abbreviated examples.
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
    strong_keywords = ['azd login', 'azd auth', 'authentication', 'credential', 'login', 'auth']
    for keyword in strong_keywords:
        if keyword in body:
            return True
    
    return False


def categorize_auth_issue(issue):
    """
    Categorize an authentication-related issue into specific subcategories.
    """
    title = issue.get('title', '').lower()
    body = issue.get('body', '').lower() if issue.get('body') else ''
    combined_text = f"{title} {body}"
    
    categories = []
    
    # WSL/Linux Authentication
    if any(keyword in combined_text for keyword in ['wsl', 'ubuntu', 'linux', 'x509', 'x.509']):
        categories.append('WSL/Linux Authentication')
    
    # Device Code Flow
    if any(keyword in combined_text for keyword in ['device code', 'device-code', 'browser', 'interactive']):
        categories.append('Device Code Flow')
    
    # Service Principal Authentication
    if any(keyword in combined_text for keyword in ['service principal', 'sp', 'pipeline', 'ci/cd', 'devops', 'automation']):
        categories.append('Service Principal Authentication')
    
    # Container/Dev Environment Authentication
    if any(keyword in combined_text for keyword in ['container', 'docker', 'codespace', 'dev container', 'jupyter']):
        categories.append('Container/Dev Environment Authentication')
    
    # Token Management
    if any(keyword in combined_text for keyword in ['token', 'refresh', 'expir', 'cache', 'credential store']):
        categories.append('Token Management')
    
    # Multi-tenant Authentication
    if any(keyword in combined_text for keyword in ['tenant', 'multi-tenant', 'cross-tenant']):
        categories.append('Multi-tenant Authentication')
    
    # Certificate Authentication
    if any(keyword in combined_text for keyword in ['certificate', 'cert', 'x509', 'x.509', 'pkcs']):
        categories.append('Certificate Authentication')
    
    # AKS/Kubernetes Authentication
    if any(keyword in combined_text for keyword in ['aks', 'kubernetes', 'k8s', 'cluster']):
        categories.append('AKS/Kubernetes Authentication')
    
    # Federated Identity
    if any(keyword in combined_text for keyword in ['federated', 'federation', 'workload identity', 'oidc']):
        categories.append('Federated Identity')
    
    # If no specific category found, use General Authentication
    if not categories:
        categories.append('General Authentication Errors')
    
    return categories


def calculate_priority_score(issue):
    """
    Calculate a priority score for an issue based on various factors.
    """
    score = 0
    
    # Base score on comments (community engagement)
    comments = issue.get('comments', 0)
    score += min(comments * 2, 20)  # Cap comment score at 20
    
    # Score based on reactions
    reactions = issue.get('reactions', {})
    if isinstance(reactions, dict):
        total_reactions = reactions.get('total_count', 0)
        score += min(total_reactions, 10)  # Cap reaction score at 10
    
    # Score based on age and activity
    try:
        created_at = issue.get('created_at', '')
        if created_at:
            created_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            days_old = (datetime.now(created_date.tzinfo) - created_date).days
            
            # Older issues that are still open get higher priority
            if issue.get('state', '') == 'open':
                if days_old > 365:
                    score += 15
                elif days_old > 180:
                    score += 10
                elif days_old > 90:
                    score += 5
        
        # Score based on recent activity
        updated_at = issue.get('updated_at', '')
        if updated_at:
            updated_date = datetime.fromisoformat(updated_at.replace('Z', '+00:00'))
            days_since_update = (datetime.now(updated_date.tzinfo) - updated_date).days
            
            if days_since_update < 30:
                score += 5
            elif days_since_update < 90:
                score += 2
        
    except:
        pass
    
    return score


def generate_complete_auth_report(data_files, output_file):
    """
    Generate a comprehensive authentication issues report with ALL issues listed.
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
                    # Categorize the issue
                    categories = categorize_auth_issue(issue)
                    issue['categories'] = categories
                    
                    # Calculate priority score
                    issue['priority_score'] = calculate_priority_score(issue)
                    
                    all_auth_issues.append(issue)
                    processed_issues.add(issue_number)
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    print(f"Total authentication issues found: {len(all_auth_issues)}")
    
    # Filter to only open issues
    all_auth_issues = [issue for issue in all_auth_issues if issue.get('state', '') == 'open']
    print(f"Open authentication issues: {len(all_auth_issues)}")
    
    # Sort issues by priority score
    all_auth_issues.sort(key=lambda x: -x.get('priority_score', 0))
    
    # Generate category statistics
    category_stats = defaultdict(int)
    for issue in all_auth_issues:
        for category in issue.get('categories', []):
            category_stats[category] += 1
    
    # Sort categories by count
    sorted_categories = sorted(category_stats.items(), key=lambda x: -x[1])
    
    # Since we're only working with open issues now
    open_issues = all_auth_issues
    
    # Get recent issues (last 90 days)
    now = datetime.now()
    recent_cutoff = now - timedelta(days=90)
    recent_issues = []
    
    for issue in open_issues:
        try:
            created_at = issue.get('created_at', '')
            if created_at:
                created_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                if created_date.replace(tzinfo=None) > recent_cutoff:
                    recent_issues.append(issue)
        except:
            continue
    
    # Get most active issues
    most_active = sorted(open_issues, key=lambda x: -x.get('comments', 0))
    
    # Generate report content
    total_issues = len(open_issues)
    
    report_content = f"""# Azure Developer CLI (azd) - Open Authentication Issues Complete Analysis

**Generated:** {now.strftime('%B %d, %Y')}  
**Repository:** Azure/azure-dev  
**Focus:** Open Authentication, Login, and Credential Management Issues  
**Analysis Period:** July 2022 - July 2025

## Executive Summary

This report provides a **COMPLETE** analysis of open authentication-related issues in the Azure Developer CLI repository, listing ALL identified open issues in each category rather than providing abbreviated examples.

### Key Metrics

- **Total Open Authentication Issues:** {len(open_issues)} issues identified
- **Recent Issues (Last 90 Days):** {len(recent_issues)}
- **Categories Identified:** {len(category_stats)}

### Authentication Categories Overview

"""
    
    for category, count in sorted_categories:
        percentage = (count / total_issues) * 100
        report_content += f"- **{category}:** {count} issues ({percentage:.1f}%)\n"
    
    report_content += f"""

## Complete Authentication Issues by Category

> **Note:** This appendix provides the **complete list** of all authentication issues identified in each category. Every issue found in the analysis is listed below.

"""
    
    # Add complete categorized listings
    for category, count in sorted_categories:
        if count == 0:
            continue
            
        report_content += f"\n### {category} ({count} issues)\n\n"
        category_issues = [issue for issue in all_auth_issues if category in issue.get('categories', [])]
        category_issues.sort(key=lambda x: -x.get('priority_score', 0))
        
        # List ALL issues in the category (no limit)
        for issue in category_issues:
            number = issue.get('number', 'N/A')
            title = issue.get('title', 'No title')
            state = issue.get('state', 'unknown')
            comments = issue.get('comments', 0)
            
            # Format creation date
            created_at = issue.get('created_at', '')
            if created_at:
                try:
                    created_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    created_str = created_date.strftime('%Y-%m-%d')
                except:
                    created_str = 'Unknown'
            else:
                created_str = 'Unknown'
            
            report_content += f"- [#{number}](https://github.com/Azure/azure-dev/issues/{number}) {title} (Created: {created_str}, State: {state}, Comments: {comments})\n"
    
    report_content += f"""

---

**Report Generation Details:**
- **Generated on:** {now.strftime('%Y-%m-%d %H:%M:%S')}
- **Data sources:** GitHub Issues API data from azure-dev repository
- **Analysis method:** Comprehensive automated categorization and priority scoring
- **Issue identification:** Keyword-based matching for authentication-related content
- **Completeness:** This report lists ALL identified authentication issues, not abbreviated examples

*This report provides complete visibility into authentication-related challenges in the Azure Developer CLI project.*
"""
    
    # Write report to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"Complete open authentication issues report generated: {output_file}")
    print(f"Total open authentication issues: {total_issues}")
    print(f"Categories found: {len(category_stats)}")


def main():
    parser = argparse.ArgumentParser(description='Extract ALL authentication issues from Azure Dev CLI data')
    parser.add_argument('--data-dir', default='data/raw-data', 
                       help='Directory containing JSON data files')
    parser.add_argument('--output', default='../reports/authentication-issues-complete.md',
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
    print("Starting complete authentication issues extraction...")
    generate_complete_auth_report(data_files, args.output)
    print("Complete authentication issues analysis finished!")


if __name__ == '__main__':
    main()
