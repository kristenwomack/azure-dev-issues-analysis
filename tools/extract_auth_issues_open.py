#!/usr/bin/env python3

"""
Extract OPEN authentication-related issues from Azure Dev CLI GitHub repository data.
Creates a focused report listing only open issues for work organization.
"""

import json
import os
from datetime import datetime
from collections import defaultdict

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

    auth_labels = ['authn', 'auth', 'authentication', 'login', 'credential']

    title = issue.get('title', '').lower()
    body = issue.get('body', '').lower() if issue.get('body') else ''
    labels = [label.get('name', '').lower() for label in issue.get('labels', [])]

    for keyword in auth_keywords:
        if keyword in title or keyword in body:
            return True

    for label in labels:
        if any(auth_label in label for auth_label in auth_labels):
            return True

    return False

def categorize_issue(issue):
    """
    Categorize an authentication issue based on its content and labels.
    """
    categories = set()
    title = issue.get('title', '').lower()
    body = issue.get('body', '').lower() if issue.get('body') else ''

    category_keywords = {
        'Service Principal Authentication': ['service principal', 'sp auth', 'client id', 'client secret'],
        'Container/Dev Environment Authentication': ['container', 'devcontainer', 'codespace', 'cloud shell'],
        'Token Management': ['token', 'refresh', 'access token', 'bearer'],
        'WSL/Linux Authentication': ['wsl', 'linux', 'ubuntu', 'debian'],
        'Device Code Flow': ['device', 'device code', 'browser'],
        'AKS/Kubernetes Authentication': ['aks', 'kubernetes', 'cluster'],
        'Multi-tenant Authentication': ['tenant', 'multi-tenant', 'organization'],
        'Federated Identity': ['federated', 'federation', 'workload identity'],
        'SAML/SSO': ['saml', 'sso', 'single sign'],
        'General Authentication Errors': ['error', 'fail', 'cannot', 'issue', 'problem']
    }

    content = f"{title} {body}"
    for category, keywords in category_keywords.items():
        if any(keyword in content for keyword in keywords):
            categories.add(category)

    return categories

def process_issues(data_dir):
    """
    Process all JSON files in the data directory and extract authentication issues.
    """
    auth_issues = []
    seen_issues = set()
    general_issues = set()
    other_category_issues = set()

    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            print(f"Processing: {os.path.join(data_dir, filename)}")
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, dict):
                        items = data.get('items', [])
                    elif isinstance(data, list):
                        items = data
                    else:
                        continue

                    for issue in items:
                        issue_number = issue.get('number')
                        if issue_number not in seen_issues and is_auth_related(issue):
                            if issue.get('state') == 'open':  # Only include open issues
                                categories = categorize_issue(issue)
                                
                                # Track issues by category
                                if 'General Authentication Errors' in categories:
                                    general_issues.add(issue_number)
                                if len(categories - {'General Authentication Errors'}) > 0:
                                    other_category_issues.add(issue_number)

                                auth_issues.append((issue, categories))
                                seen_issues.add(issue_number)

                except Exception as e:
                    print(f"Error processing {filename}: {e}")
                    continue

    # Filter out general issues that appear in other categories
    filtered_issues = []
    for issue, categories in auth_issues:
        if issue['number'] in general_issues and issue['number'] in other_category_issues:
            # Remove General category if issue appears in other categories
            categories.discard('General Authentication Errors')
        filtered_issues.append((issue, categories))

    return filtered_issues

def generate_report(issue_data, output_file):
    """
    Generate a markdown report focused on open authentication issues.
    """
    today = datetime.now()

    # Collect categories
    all_categories = defaultdict(list)
    for issue, categories in issue_data:
        for category in categories:
            all_categories[category].append(issue)

    # Generate report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Azure Developer CLI (azd) - Open Authentication Issues Analysis\n\n")
        f.write(f"**Generated:** {today.strftime('%B %d, %Y')}  \n")
        f.write("**Repository:** Azure/azure-dev  \n")
        f.write("**Focus:** Open Authentication, Login, and Credential Management Issues  \n\n")

        f.write("## Executive Summary\n\n")
        f.write("This report focuses on **OPEN** authentication-related issues in the Azure Developer CLI repository ")
        f.write("to facilitate work organization and prioritization.\n\n")

        f.write("### Key Metrics\n\n")
        total_issues = len(set(issue['number'] for issue, _ in issue_data))
        f.write(f"- **Total Open Authentication Issues:** {total_issues} issues\n")
        recent_issues = sum(1 for issue, _ in issue_data if (today - datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ')).days <= 90)
        f.write(f"- **Recent Issues (Last 90 Days):** {recent_issues}\n")
        f.write(f"- **Categories Identified:** {len(all_categories)}\n\n")

        f.write("### Authentication Categories Overview\n\n")
        f.write("| Category | Issues | Percentage |\n")
        f.write("|----------|---------|------------|\n")
        for category, category_issues in sorted(all_categories.items(), key=lambda x: len(x[1]), reverse=True):
            percentage = (len(category_issues) / total_issues) * 100
            f.write(f"| {category} | {len(category_issues)} | {percentage:.1f}% |\n")

        f.write("\n## Detailed Category Analysis\n\n")
        for category, category_issues in sorted(all_categories.items(), key=lambda x: len(x[1]), reverse=True):
            f.write(f"\n### {category}\n\n")
            f.write(f"**Total Open Issues:** {len(category_issues)}\n\n")

            # Create table header
            f.write("| Issue | Number | Created | Labels |\n")
            f.write("|-------|---------|---------|--------|\n")

            # Add table rows
            for issue in sorted(category_issues, key=lambda x: x['created_at'], reverse=True):
                created_date = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
                title_link = f"[{issue['title']}]({issue['html_url']})"
                issue_number = f"#{issue['number']}"
                labels = "`none`"
                if issue.get('labels'):
                    labels = ", ".join([f"`{label['name']}`" for label in issue['labels']])
                f.write(f"| {title_link} | {issue_number} | {created_date} | {labels} |\n")

def main():
    print("Starting open authentication issues extraction...")
    data_dir = "data/raw-data"
    output_file = "../reports/authentication-issues-open.md"

    auth_issues = process_issues(data_dir)
    print(f"\nTotal open authentication issues found: {len(set(issue['number'] for issue, _ in auth_issues))}")

    generate_report(auth_issues, output_file)
    print(f"Open authentication issues report generated: {output_file}")
    print("Analysis of open authentication issues finished!")

if __name__ == "__main__":
    main()