# Multi-Environment Workflow Issues Analysis

## Azure Developer CLI - Environment Promotion and Workflow Challenges

**Report Generated:** August 6, 2025  
**Source:** environment-issues-detailed-20250721.md  
**Focus:** Multi-Environment Workflows - Users struggle with promoting between dev/staging/prod environments  

## Executive Summary

This report analyzes issues specifically related to multi-environment workflows in Azure Developer CLI, where users face challenges promoting applications and configurations between development, staging, and production environments. Issues are clustered by similarity.

**Total Issues Analyzed:** 17 issues (19 recent issues excluded)  
**Issue Categories:** 5 main clusters  
**Note:** Issues logged by Wallace in the last 90 days have been excluded from this analysis to focus on historical patterns and customer-reported issues.  

---

## Cluster 1: Environment Type System and Configuration

Issues related to environment type definitions, configuration management, and environment-specific settings

*Note: Several recent team issues (5311, 5316, 5318, 5396, 5317, 5315, 5314, 5313) have been excluded from this analysis.*

---

## Cluster 2: Environment Promotion and Deployment Workflows

Issues focused on promoting code and infrastructure between environments

| Issue # | Title | Created | Age (Days) | Comments | Reporter | Labels | Notes |
|---------|-------|---------|------------|----------|----------|--------|-------|
| [4739](https://github.com/Azure/azure-dev/issues/4739) | [Issue] azd provision and azd deploy Seem to Ignore AZD_INITIAL_ENVIRONMENT_CONF... | 2025-01-29 | 173 | 7 | Customer | question, pipelines, customer-reported | This is a closed issue. No action taken. |
| [3180](https://github.com/Azure/azure-dev/issues/3180) | Deployment iteration ID as environment variable | 2024-01-07 | 561 | 5 | Customer | enhancement, question, customer-reported | Documented here: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/environment-variables-faq. Closing issue.
| [5034](https://github.com/Azure/azure-dev/issues/5034) | Identify gaps/features: E2E/Production readiness | 2025-04-02 | 109 | 1 | Team | production | This is already closed. No action taken.
| [3297](https://github.com/Azure/azure-dev/issues/3297) | Multi-environment scenarios do not work | 2024-02-06 | 531 | 1 | Customer | bug, vs, aspire | This is already closed. No action taken.
| [3550](https://github.com/Azure/azure-dev/issues/3550) | [Issue] Create Resource Group Deployment Based on Environment Variable | 2024-03-18 | 490 | 0 | Customer | feature, aspire | Now closed. Victor confirmed: "This is not supported publishing Aspire projects. And to support this, it should be possible to model this from Aspire (the AppHost). I'll create dotnet/aspire#11037 to follow up with Aspire team"

*Note: Recent issues (5472, 5335, 5346) have been excluded from this analysis.*

---

## Cluster 3: Dev-to-Production Workflow Documentation and Tooling

Issues related to dev-to-prod workflows, documentation gaps, and production readiness

*Note: Recent team documentation issues (5483, 5482, 5427) have been excluded from this analysis.*

---

## Cluster 4: CI/CD Pipeline Integration and Environment-Specific Deployments

Issues related to integrating environments with CI/CD pipelines and automated deployments

| Issue # | Title | Created | Age (Days) | Comments | Reporter | Labels | Notes |
|---------|-------|---------|------------|----------|----------|--------|-------|
| [4347](https://github.com/Azure/azure-dev/issues/4347) | Fail to run `azd pipeline config --provider github` and `azd pipeline config --p... | 2024-09-19 | 305 | 11 | Customer | terraform, pipelines | Now closed. Victor: "azd supports Federated Credentials now for Terraform as well and people can use this instead of secret credentials."
| [4348](https://github.com/Azure/azure-dev/issues/4348) | Fail to run `azd pipeline config --provider azdo` for `todo-nodejs-mongo-aks` | 2024-09-19 | 305 | 9 | Customer | bug, templates, azdo | Closed. Transferred to https://github.com/Azure-Samples/todo-nodejs-mongo-aks/issues/16.
| [4248](https://github.com/Azure/azure-dev/issues/4248) | [Issue]azd pipeline config could not find a default agent queue in project | 2024-08-26 | 329 | 6 | Customer | enhancement, question, azdo | Check with Victor. Still issue. He will look into this.
| [3920](https://github.com/Azure/azure-dev/issues/3920) | Project hooks don't work when there's not environment, like in CI/CD | 2024-05-16 | 430 | 4 | Customer | bug, pipelines, hooks | Checked with Victor. Still issue. He will look into this.
| [4197](https://github.com/Azure/azure-dev/issues/4197) | [pipeline config] Add one-time confirmation for the remote | 2024-08-09 | 346 | 2 | Team | enhancement, pipelines | Not related to environment. This is an `azd pipeline config` enhancement to avoid hitting issue when customer `azd pipeline config` an azd project. Customers do not have access to configure CICD since remote is set to the project repro.
| [3957](https://github.com/Azure/azure-dev/issues/3957) | Questions Regarding Best Practices for CI/CD with Aspire | 2024-05-27 | 420 | 2 | Customer | question, pipelines, customer-reported | Aspire best practiced. Follow up separately.
| [4103](https://github.com/Azure/azure-dev/issues/4103) | [pipeline config] [Aspire] When running within AppHost for a new project, the .g... | 2024-07-11 | 375 | 1 | Team | pipelines, aspire | Aspire-related.
| [3641](https://github.com/Azure/azure-dev/issues/3641) | [todo-templ] Running `azd pipeline config`, an error occurred in the pipeline | 2024-04-03 | 474 | 1 | Customer | bug, pipelines | Victor closed this "closing as aged. No more repro reported and things around auth in pipelines work differently now than 2 years ago"
| [5221](https://github.com/Azure/azure-dev/issues/5221) | Improve the experience for `pipeline config` for Tenants where applicationServic... | 2025-05-27 | 55 | 0 | Team | pipelines | Victor has fixed and closed this 8/21/25.
| [5186](https://github.com/Azure/azure-dev/issues/5186) | [.NET Aspire] pipeline config is broken when running from the AppHost from a non... | 2025-05-12 | 69 | 0 | Team | aspire | Aspire-related
| [4138](https://github.com/Azure/azure-dev/issues/4138) | Feature request: azd pipeline config --provider azdo -> to re-use existing servi... | 2024-07-22 | 364 | 0 | Customer | enhancement, question, azdo | Assigned to Alex to doc.
| [4128](https://github.com/Azure/azure-dev/issues/4128) | Let azd to ignore auth for the SP with a flag when running pipeline config | 2024-07-16 | 370 | 0 | Team | enhancement, pipelines | This is `azd pipeline config` enhancement. Not environment-related.
| [3587](https://github.com/Azure/azure-dev/issues/3587) | Allow flag to define the path of pipeline when running `azd pipeline config` | 2024-03-24 | 484 | 0 | Team | enhancement, pipelines | This is `azd pipeline config` enhancement. Not environment-related.

*Note: Recent issues (5431, 5507, 5334, 5333, 5332, 5329, 5422, 5421) have been excluded from this analysis.*

---

## Cluster 5: Environment Management and User Experience

Issues related to environment selection, switching, and overall user experience

| Issue # | Title | Created | Age (Days) | Comments | Reporter | Labels | Notes
|---------|-------|---------|------------|----------|----------|--------| ----------|
| [2434](https://github.com/Azure/azure-dev/issues/2434) | Add a note for `azd env new` for users to know that the new created environment ... | 2023-06-16 | 765 | 3 | Customer | documentation, enhancement, cli | This is a closed issue (2023.) No action taken.
| [3439](https://github.com/Azure/azure-dev/issues/3439) | [Feature] Add CLI selector to `azd env select` command | 2024-02-25 | 511 | 0 | Customer | enhancement, command, feature | This is `azd env select` enhancement. Keep in backlog.

---

## Key Insights and Patterns

### 1. Customer Pain Points Focus

With recent team issues excluded, this analysis highlights core customer-reported challenges:
- **Pipeline Configuration Failures** - Persistent issues across GitHub and Azure DevOps providers
- **Multi-Environment Support Gaps** - Fundamental workflow limitations affecting real users
- **Environment Variable Management** - Ongoing confusion around configuration precedence

### 2. Persistent Pain Points

- **Pipeline Configuration Failures** - Multiple issues spanning 2024-2025
- **Environment Variable Management** - Confusion around precedence and configuration
- **Multi-Environment Scenarios** - Fundamental challenges with environment promotion

### 3. Epic-Level Initiatives

- **Environment Configuration and Tagging** (#5310) - Comprehensive environment management
- **Advanced Deployment Strategies** (#5338) - Blue-green, staging slots, canary deployments
- **Provisioning Limitations and Layered Infrastructure** (#5290) - Complex infrastructure scenarios

## Recommendations

### Immediate Priority (Customer Impact Focus)

1. Fix pipeline configuration failures for GitHub and Azure DevOps providers
2. Resolve environment variable precedence and configuration issues  
3. Address multi-environment scenario blocking issues

### Medium Priority (Historical Issues)

1. Improve pipeline configuration user experience for complex tenant scenarios
2. Enhance Aspire integration with pipeline configuration
3. Develop better error handling and user guidance for pipeline setup

### Long-term Strategic (Based on Customer Feedback)

1. Simplify environment management and selection workflows
2. Improve documentation for multi-environment scenarios
3. Enhance support for complex deployment architectures

---

**Analysis Methodology:**

- Filtered from 840 total environment issues
- Excluded 19 issues logged by Wallace in the last 90 days
- Grouped by functional similarity and workflow impact
- Focused on dev/staging/prod promotion challenges
- Prioritized customer-reported issues and historical patterns


---

## Summary Table: Issue Categories and Links

| Category                      | # of Issues | Issue Links |
|-------------------------------|:-----------:|:------------|
| Closed with no action         |      4      | [4739](https://github.com/Azure/azure-dev/issues/4739), [5034](https://github.com/Azure/azure-dev/issues/5034), [3297](https://github.com/Azure/azure-dev/issues/3297), [2434](https://github.com/Azure/azure-dev/issues/2434) |
| Now closed                    |      3      | [3550](https://github.com/Azure/azure-dev/issues/3550), [4347](https://github.com/Azure/azure-dev/issues/4347), [5221](https://github.com/Azure/azure-dev/issues/5221) |
| Aspire-related                |      3      | [3957](https://github.com/Azure/azure-dev/issues/3957), [4103](https://github.com/Azure/azure-dev/issues/4103), [5186](https://github.com/Azure/azure-dev/issues/5186) |
| Non-environment related       |      3      | [4197](https://github.com/Azure/azure-dev/issues/4197), [4128](https://github.com/Azure/azure-dev/issues/4128), [3587](https://github.com/Azure/azure-dev/issues/3587) |
| Backlog/Assigned/Follow-up    |      2      | [3439](https://github.com/Azure/azure-dev/issues/3439), [4138](https://github.com/Azure/azure-dev/issues/4138) |
| Still open/investigating      |      2      | [4248](https://github.com/Azure/azure-dev/issues/4248), [3920](https://github.com/Azure/azure-dev/issues/3920) |
| Aged/no more repro            |      1      | [3641](https://github.com/Azure/azure-dev/issues/3641) |
| Closed (Transferred/Documented)|     2      | [4348](https://github.com/Azure/azure-dev/issues/4348), [3180](https://github.com/Azure/azure-dev/issues/3180) |

*This table summarizes the distribution of all 20 issues by category, with direct links for reference.*
