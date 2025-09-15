# Azure Developer CLI (azd) - Open Authentication Issues Analysis

**Generated:** September 15, 2025  
**Repository:** Azure/azure-dev  
**Focus:** Open Authentication, Login, and Credential Management Issues  

## Executive Summary

This report focuses on **OPEN** authentication-related issues in the Azure Developer CLI repository to facilitate work organization and prioritization.

### Key Metrics

- **Total Open Authentication Issues:** 210 issues
- **Recent Issues (Last 90 Days):** 54
- **Categories Identified:** 10

### Authentication Categories Overview

| Category | Issues | Percentage |
|----------|---------|------------|
| Container/Dev Environment Authentication | 71 | 33.8% |
| General Authentication Errors | 47 | 22.4% |
| AKS/Kubernetes Authentication | 23 | 11.0% |
| Multi-tenant Authentication | 19 | 9.0% |
| Token Management | 15 | 7.1% |
| WSL/Linux Authentication | 14 | 6.7% |
| Device Code Flow | 8 | 3.8% |
| SAML/SSO | 7 | 3.3% |
| Service Principal Authentication | 7 | 3.3% |
| Federated Identity | 5 | 2.4% |

## Detailed Category Analysis


### Container/Dev Environment Authentication

**Total Open Issues:** 71

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template parameters](https://github.com/Azure/azure-dev/issues/5507) | #5507 | 2025-07-20 | `question`, `customer-reported` |
| [[Issue] Problem deploying a simple static HTML app to SWA using azd](https://github.com/Azure/azure-dev/issues/5506) | #5506 | 2025-07-18 | `none` |
| [Missing validation when reusing Foundry project impacts published accelerator templates (model availability, quota, and access checks)](https://github.com/Azure/azure-dev/issues/5480) | #5480 | 2025-07-15 | `none` |
| [Dynamic Region Filtering Based on User-Specified Model and Capacity on azd Quota check](https://github.com/Azure/azure-dev/issues/5432) | #5432 | 2025-07-03 | `enhancement` |
| [Fail to run `azd pipeline config` for terraform templates](https://github.com/Azure/azure-dev/issues/5422) | #5422 | 2025-07-01 | `none` |
| [Running `azd pipeline config --provider github` does not trigger actions on Codespaces](https://github.com/Azure/azure-dev/issues/5421) | #5421 | 2025-07-01 | `bug`, `codespaces`, `pipelines` |
| [SPIKE: determine LLM access options for azd](https://github.com/Azure/azure-dev/issues/5375) | #5375 | 2025-06-18 | `none` |
| [Add traffic splitting automation](https://github.com/Azure/azure-dev/issues/5354) | #5354 | 2025-06-17 | `none` |
| [Container Apps Revision Strategy](https://github.com/Azure/azure-dev/issues/5352) | #5352 | 2025-06-17 | `none` |
| [Epic: Advanced Deployment Strategies](https://github.com/Azure/azure-dev/issues/5338) | #5338 | 2025-06-17 | `epic`, `app service`, `aca`, `production` |
| [`azd monitor --live` fails to connect: "could not connect to your application"](https://github.com/Azure/azure-dev/issues/5235) | #5235 | 2025-05-29 | `templates`, `terraform`, `monitor` |
| [[Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in Azure DevOps with WIF, Despite principalId Configuration](https://github.com/Azure/azure-dev/issues/5201) | #5201 | 2025-05-15 | `question`, `pipelines`, `customer-reported`, `aspire` |
| [Missing Documentation on Remote Builds for Docker Image w/ ACR](https://github.com/Azure/azure-dev/issues/5156) | #5156 | 2025-05-05 | `documentation` |
| [Australia Southeast Aspire Dashboard failing](https://github.com/Azure/azure-dev/issues/5150) | #5150 | 2025-05-02 | `question`, `customer-reported` |
| [BUG : azd deploy do not use the same API version than defined in the BICEP file for Microsoft.App/containerApps](https://github.com/Azure/azure-dev/issues/5109) | #5109 | 2025-04-22 | `question`, `customer-reported` |
| [compose: static site support](https://github.com/Azure/azure-dev/issues/5094) | #5094 | 2025-04-17 | `compose` |
| [[Issue] Anonymous volume mounts in Aspire cause deployment breaks](https://github.com/Azure/azure-dev/issues/5058) | #5058 | 2025-04-08 | `aspire` |
| [compose: App Service - containerless/runtime-specific support](https://github.com/Azure/azure-dev/issues/5050) | #5050 | 2025-04-07 | `compose` |
| [[Issue] container image push failure during azd up - error code 51, network connectivity or timeout issue](https://github.com/Azure/azure-dev/issues/5005) | #5005 | 2025-03-31 | `easy-init` |
| [[Issue] If service name has spaces, bicep will produce environment variable names with space also](https://github.com/Azure/azure-dev/issues/4996) | #4996 | 2025-03-27 | `bug`, `core` |
| [azd up does not enable data protection for Aspire App](https://github.com/Azure/azure-dev/issues/4949) | #4949 | 2025-03-17 | `question`, `customer-reported` |
| [compose: provisioned resource(s) naming](https://github.com/Azure/azure-dev/issues/4915) | #4915 | 2025-03-08 | `compose` |
| [Feature: Keep plain text in env value in azure.yaml](https://github.com/Azure/azure-dev/issues/4911) | #4911 | 2025-03-07 | `Bicep`, `compose` |
| [Remote state does not work when user has multiple tenants.](https://github.com/Azure/azure-dev/issues/4903) | #4903 | 2025-03-06 | `remote-env` |
| [compose: cosmos db - containers](https://github.com/Azure/azure-dev/issues/4837) | #4837 | 2025-02-21 | `discuss` |
| [AZD Remote environment with Terraform local backend](https://github.com/Azure/azure-dev/issues/4756) | #4756 | 2025-02-03 | `terraform`, `remote-env` |
| [compose: explicit mapping](https://github.com/Azure/azure-dev/issues/4747) | #4747 | 2025-01-31 | `design`, `compose` |
| [[Issue] Failed to deploy app when app name too long or different app name has same long prefix](https://github.com/Azure/azure-dev/issues/4653) | #4653 | 2024-12-26 | `compose` |
| [Unable to run tenant level deployments](https://github.com/Azure/azure-dev/issues/4643) | #4643 | 2024-12-20 | `Bicep`, `core` |
| [[Issue] After `azd init` help user with common application tasks](https://github.com/Azure/azure-dev/issues/4607) | #4607 | 2024-12-04 | `enhancement`, `easy-init` |
| [[Enhacement] Include branch name when checking pipeline existence](https://github.com/Azure/azure-dev/issues/4566) | #4566 | 2024-11-18 | `question`, `azdo`, `pipelines`, `customer-reported`, `aspire` |
| [Template test pipeline handling of terraform tests](https://github.com/Azure/azure-dev/issues/4528) | #4528 | 2024-11-07 | `templates`, `terraform`, `pipelines` |
| [Remove ASA Support from AZD](https://github.com/Azure/azure-dev/issues/4504) | #4504 | 2024-10-31 | `asa` |
| [Analysis of GitHub issues by tag](https://github.com/Azure/azure-dev/issues/4445) | #4445 | 2024-10-16 | `pm` |
| [proposal: incremental `azd up`](https://github.com/Azure/azure-dev/issues/4366) | #4366 | 2024-09-20 | `enhancement`, `inner loop` |
| [[WebToolsE2E][Aspire][GB18030] An error occurs when deploying an Aspire project that uses Chinese characters as the project name.](https://github.com/Azure/azure-dev/issues/4360) | #4360 | 2024-09-20 | `bug`, `question`, `customer-reported`, `aspire` |
| [Fail to run `azd pipeline config --provider github` and `azd pipeline config --provider azdo`](https://github.com/Azure/azure-dev/issues/4347) | #4347 | 2024-09-19 | `terraform`, `pipelines` |
| [Fail to load web page when `start api and web` in Devcontainer](https://github.com/Azure/azure-dev/issues/4346) | #4346 | 2024-09-19 | `bug`, `templates`, `terraform` |
| [Split container app deployment out from provisioning](https://github.com/Azure/azure-dev/issues/4232) | #4232 | 2024-08-21 | `discuss`, `aca` |
| [[pipeline config] Add one-time confirmation for the remote](https://github.com/Azure/azure-dev/issues/4197) | #4197 | 2024-08-09 | `enhancement`, `pipelines` |
| [[Issue] Prepackage hooks runs after building the docker image the first time](https://github.com/Azure/azure-dev/issues/4136) | #4136 | 2024-07-22 | `question`, `customer-reported`, `hooks` |
| [[Feature] azd provision only deploying changed infra](https://github.com/Azure/azure-dev/issues/4123) | #4123 | 2024-07-15 | `enhancement`, `command`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [Questions Regarding Best Practices for CI/CD with Aspire](https://github.com/Azure/azure-dev/issues/3957) | #3957 | 2024-05-27 | `question`, `pipelines`, `customer-reported`, `needs-team-attention`, `aspire` |
| [Azure resources cannot depend on project resources](https://github.com/Azure/azure-dev/issues/3931) | #3931 | 2024-05-18 | `enhancement`, `core`, `aspire` |
| [[Issue] HashConflictOnDifferentRoleAssignmentIds error for Core bicep file](https://github.com/Azure/azure-dev/issues/3878) | #3878 | 2024-05-08 | `iac`, `Bicep` |
| [[Issue] Remote end - `InvalidAuthenticationInfo`](https://github.com/Azure/azure-dev/issues/3808) | #3808 | 2024-04-28 | `question`, `terraform`, `customer-reported`, `needs-team-attention`, `remote-env` |
| [azd package fails after installing buildx](https://github.com/Azure/azure-dev/issues/3807) | #3807 | 2024-04-27 | `command`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [[Issue] --use-device-code auth flow presents the wrong app name](https://github.com/Azure/azure-dev/issues/3742) | #3742 | 2024-04-18 | `cli`, `core` |
| [[remote env] error for short template name](https://github.com/Azure/azure-dev/issues/3713) | #3713 | 2024-04-15 | `core`, `aspire`, `remote-env` |
| [[Issue] Support build arguments for the azd deploy section](https://github.com/Azure/azure-dev/issues/3710) | #3710 | 2024-04-15 | `command`, `extensibility`, `core` |
| [[Issue] azd not installed correctly on mac m1 dev container for ](https://github.com/Azure/azure-dev/issues/3707) | #3707 | 2024-04-13 | `bug`, `engsys`, `question`, `installer`, `customer-reported`, `needs-team-attention` |
| [[Issue] Azure Functions deployment does not work well in the case of a monorepo](https://github.com/Azure/azure-dev/issues/3697) | #3697 | 2024-04-12 | `pm`, `feature` |
| [[todo-templ] Running `azd pipeline config`, an error occurred in the pipeline](https://github.com/Azure/azure-dev/issues/3641) | #3641 | 2024-04-03 | `bug`, `pipelines` |
| [[Issue] Changing the `name` property did not deploy to new namespace](https://github.com/Azure/azure-dev/issues/3590) | #3590 | 2024-03-25 | `bug`, `aks` |
| [[Issue] azd up should warn on potentially destructive changes when target resources exist and instead try to patch them](https://github.com/Azure/azure-dev/issues/3512) | #3512 | 2024-03-08 | `enhancement`, `question`, `customer-reported`, `needs-team-attention`, `core`, `aspire` |
| [[Issue] Azure env variables not exported during packaging](https://github.com/Azure/azure-dev/issues/3456) | #3456 | 2024-02-29 | `command`, `feature`, `core` |
| [Ability to pass output from first service into the 2nd service, so the 2nd service can connect to the 1st service:](https://github.com/Azure/azure-dev/issues/3401) | #3401 | 2024-02-20 | `enhancement`, `core` |
| [Create public documentation for developer expectations when using each supported service target or language](https://github.com/Azure/azure-dev/issues/3363) | #3363 | 2024-02-14 | `documentation` |
| [[Issue] Deployment failed: failing invoking action 'provision', error deploying infrastructure: deploying to subscription: In Azure i can see 502 (Bad Gateway) (Code: ValidationError, Target: representation)](https://github.com/Azure/azure-dev/issues/3350) | #3350 | 2024-02-13 | `command`, `question`, `customer-reported`, `github actions`, `core` |
| [It should be possible to customize Docker image names created with azd deploy](https://github.com/Azure/azure-dev/issues/3335) | #3335 | 2024-02-10 | `enhancement`, `question`, `customer-reported`, `needs-team-attention`, `aca`, `aspire` |
| [Support for optional containers configuration section for container based service targ](https://github.com/Azure/azure-dev/issues/3239) | #3239 | 2024-01-27 | `aks`, `aca` |
| [Support to reference multiple container projects](https://github.com/Azure/azure-dev/issues/3236) | #3236 | 2024-01-27 | `aks`, `aca` |
| [[Spike] improve azure container app deployments to avoid error-prone and confusing multiple revisions](https://github.com/Azure/azure-dev/issues/3116) | #3116 | 2023-12-13 | `question`, `customer-reported`, `needs-team-attention`, `aca` |
| [[Issue] Deploy failed to SWA with Still in WaitingForDeployment state](https://github.com/Azure/azure-dev/issues/3074) | #3074 | 2023-12-06 | `bug`, `command`, `question`, `customer-reported`, `core` |
| [`up` or other commands could fail from partially completed `init`](https://github.com/Azure/azure-dev/issues/3053) | #3053 | 2023-12-03 | `aspire` |
| [[Issue] Azd provision fails saying still provisioning from last provision which failed on postprovision script](https://github.com/Azure/azure-dev/issues/2977) | #2977 | 2023-11-15 | `command`, `question`, `customer-reported`, `core`, `hooks` |
| [[Issue] app crash when container app language is not specified](https://github.com/Azure/azure-dev/issues/2935) | #2935 | 2023-11-06 | `error handling`, `aca` |
| [[Feature] Support for deploying App Container Jobs](https://github.com/Azure/azure-dev/issues/2743) | #2743 | 2023-09-14 | `feature`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [[Issue] Specify azure.yaml for azd up](https://github.com/Azure/azure-dev/issues/2736) | #2736 | 2023-09-12 | `feature`, `core` |
| [[Issue] azd in dev container on Mac M1 - azd fails](https://github.com/Azure/azure-dev/issues/2593) | #2593 | 2023-08-03 | `bug`, `question`, `installer`, `customer-reported`, `Bicep` |
| [Add subscription/region selection to `azd env refresh`?](https://github.com/Azure/azure-dev/issues/2415) | #2415 | 2023-06-14 | `discuss`, `hacktoberfest` |

### General Authentication Errors

**Total Open Issues:** 47

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Command runner logging enhancements with `--debug`](https://github.com/Azure/azure-dev/issues/5502) | #5502 | 2025-07-17 | `enhancement` |
| [[Issue] I need to define two services to deploy to host if my host is included in two scale units deployed to different regions](https://github.com/Azure/azure-dev/issues/5472) | #5472 | 2025-07-10 | `documentation`, `production` |
| [[Issue] deployment failed: Input string was not in a correct format.](https://github.com/Azure/azure-dev/issues/5406) | #5406 | 2025-06-25 | `functions`, `app service` |
| [EPIC: agent-powered troubleshooting](https://github.com/Azure/azure-dev/issues/5374) | #5374 | 2025-06-18 | `epic` |
| [Create traffic shifting capabilities](https://github.com/Azure/azure-dev/issues/5348) | #5348 | 2025-06-17 | `none` |
| [Add configuration validation for merged files](https://github.com/Azure/azure-dev/issues/5321) | #5321 | 2025-06-16 | `none` |
| [Implement YAML file parsing and merging](https://github.com/Azure/azure-dev/issues/5320) | #5320 | 2025-06-16 | `none` |
| [Layered Configuration Files](https://github.com/Azure/azure-dev/issues/5318) | #5318 | 2025-06-16 | `none` |
| [Implement `--type` flag for `azd env new` command](https://github.com/Azure/azure-dev/issues/5314) | #5314 | 2025-06-16 | `none` |
| [Epic: Environment Configuration and Tagging](https://github.com/Azure/azure-dev/issues/5310) | #5310 | 2025-06-16 | `epic`, `remote-env`, `production` |
| [Multi-Provider Infrastructure Support](https://github.com/Azure/azure-dev/issues/5298) | #5298 | 2025-06-16 | `none` |
| [Epic: Provisioning Limitations and Layered Infrastructure](https://github.com/Azure/azure-dev/issues/5290) | #5290 | 2025-06-16 | `iac`, `epic`, `production` |
| [[.NET Aspire] pipeline config is broken when running from the AppHost from a non-git fresh project](https://github.com/Azure/azure-dev/issues/5186) | #5186 | 2025-05-12 | `aspire` |
| [Improve error message for duplicate `azd-service-name` tags](https://github.com/Azure/azure-dev/issues/5152) | #5152 | 2025-05-02 | `core` |
| [[Issue] Logging doesn't always appear in App Insights and Log Analytics after taking down an environment and redeploying it](https://github.com/Azure/azure-dev/issues/5080) | #5080 | 2025-04-12 | `question`, `customer-reported` |
| [[Issue] Feature Request: Handoff Function App keys easier ex: 'mcp_extension' Key](https://github.com/Azure/azure-dev/issues/5047) | #5047 | 2025-04-04 | `functions`, `mcp` |
| [`azd ext source remove` with no arguments panics](https://github.com/Azure/azure-dev/issues/5037) | #5037 | 2025-04-02 | `extensibility`, `extensions` |
| [[AI Extension] Error at the end of the prompts](https://github.com/Azure/azure-dev/issues/4975) | #4975 | 2025-03-23 | `extensions` |
| [compose: show UX enhancements](https://github.com/Azure/azure-dev/issues/4933) | #4933 | 2025-03-12 | `compose` |
| [[Issue] Error archive/tar: write too long when using ACA remoteBuild](https://github.com/Azure/azure-dev/issues/4803) | #4803 | 2025-02-17 | `bug` |
| [[Issue] azd down does not delete the app registration defined using the Bicep Graph provider](https://github.com/Azure/azure-dev/issues/4724) | #4724 | 2025-01-23 | `command`, `feature`, `question`, `customer-reported`, `needs-team-attention`, `Bicep`, `core` |
| [compose: ability to add Azure resource in a different resource group from my app](https://github.com/Azure/azure-dev/issues/4543) | #4543 | 2024-11-12 | `compose` |
| [[Issue] azd template list in DevCenter mode fails silently when not logged in](https://github.com/Azure/azure-dev/issues/4485) | #4485 | 2024-10-24 | `templates`, `ade` |
| [[FEATURE REQUEST] Ability to inject custom tags](https://github.com/Azure/azure-dev/issues/4479) | #4479 | 2024-10-23 | `feature`, `discuss`, `needs-triage`, `needs-team-attention` |
| [package: support ignore files](https://github.com/Azure/azure-dev/issues/4381) | #4381 | 2024-09-26 | `feature` |
| [Fail to run task `start api` for `todo-python-mongo-swa-func` on Mac env](https://github.com/Azure/azure-dev/issues/4274) | #4274 | 2024-08-30 | `templates`, `vscode`, `inner loop` |
| [[Issue] Running `azd deploy` within an .NET Aspire app deploy all the services](https://github.com/Azure/azure-dev/issues/4133) | #4133 | 2024-07-19 | `enhancement`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [Fail to start api for `todo-python-mongo` when default terminal is `Git Bash` in Windows](https://github.com/Azure/azure-dev/issues/4127) | #4127 | 2024-07-16 | `vs`, `vscode`, `terraform` |
| [[Feature request] Add `manual` or `workflow_dispatch` flag to hooks to allow for selective execution of hooks](https://github.com/Azure/azure-dev/issues/3981) | #3981 | 2024-06-05 | `enhancement`, `question`, `customer-reported`, `needs-team-attention`, `hooks` |
| [[Issue] Bash (MINGW64) doesn't show subscription list during `azd up`](https://github.com/Azure/azure-dev/issues/3932) | #3932 | 2024-05-19 | `cli`, `feature` |
| [Project hooks don't work when there's not environment, like in CI/CD](https://github.com/Azure/azure-dev/issues/3920) | #3920 | 2024-05-16 | `bug`, `pipelines`, `hooks` |
| [[Aspire] Return an error when AppHost defines an azd built-in parameter](https://github.com/Azure/azure-dev/issues/3867) | #3867 | 2024-05-07 | `enhancement`, `aspire` |
| [azd infra synth fails with a project may only contain a single Aspire service and no other services at this time](https://github.com/Azure/azure-dev/issues/3812) | #3812 | 2024-04-29 | `question`, `customer-reported`, `aspire` |
| [[Issue] azd doesn't seem to like certain characters in the path to bicep.exe](https://github.com/Azure/azure-dev/issues/3810) | #3810 | 2024-04-29 | `bug`, `question`, `iac`, `customer-reported`, `needs-team-attention`, `Bicep` |
| [[WebToolsE2E][Aspire][Unstable] Publishing Aspire project failed, it shows an exception ''resource not found: 0 resource groups with prefix or suffix with value: 'xxx''](https://github.com/Azure/azure-dev/issues/3750) | #3750 | 2024-04-19 | `vs`, `aspire` |
| [[Issue] Fail to run `azd down` after creating `apicenter` resources](https://github.com/Azure/azure-dev/issues/3631) | #3631 | 2024-04-02 | `command`, `core` |
| [[Issue] Create Resource Group Deployment Based on Environment Variable](https://github.com/Azure/azure-dev/issues/3550) | #3550 | 2024-03-18 | `feature`, `aspire` |
| [[Feature] Add CLI selector to `azd env select` command](https://github.com/Azure/azure-dev/issues/3439) | #3439 | 2024-02-25 | `enhancement`, `command`, `feature`, `core` |
| [Use Entra/AAD authentication only (azd init - "Use code in current directory" workflow)](https://github.com/Azure/azure-dev/issues/3404) | #3404 | 2024-02-20 | `enhancement`, `core`, `easy-init` |
| [Revisit/discuss azd service operation caching ](https://github.com/Azure/azure-dev/issues/3392) | #3392 | 2024-02-17 | `discuss`, `engineering item` |
| [[Issue] The typescript linting is stricter than the source code](https://github.com/Azure/azure-dev/issues/3210) | #3210 | 2024-01-19 | `templates` |
| [Feature Request - Use AZD output to set values in the Azure Functions local.settings.json file](https://github.com/Azure/azure-dev/issues/3201) | #3201 | 2024-01-16 | `command`, `feature`, `functions` |
| [[Issue] `azd hooks run --help` includes hooks and their syntax?](https://github.com/Azure/azure-dev/issues/3005) | #3005 | 2023-11-19 | `enhancement`, `question`, `customer-reported`, `needs-team-attention`, `hooks` |
| [[Issue] Running `azd completion <shell> --help` does not print help related to installing shell completions](https://github.com/Azure/azure-dev/issues/2846) | #2846 | 2023-10-09 | `enhancement`, `command`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [[Issue] Allow user to use a deployment location and resource location](https://github.com/Azure/azure-dev/issues/2823) | #2823 | 2023-10-05 | `feature`, `core` |
| [Password seeding pattern creates non-trivial deployment outputs](https://github.com/Azure/azure-dev/issues/2685) | #2685 | 2023-08-31 | `bug`, `discuss` |
| [`azd down` with a VNET/NSG, sometimes fails because NSG can't be deleted first.](https://github.com/Azure/azure-dev/issues/2497) | #2497 | 2023-07-10 | `command`, `templates`, `error handling`, `core` |

### AKS/Kubernetes Authentication

**Total Open Issues:** 23

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template parameters](https://github.com/Azure/azure-dev/issues/5507) | #5507 | 2025-07-20 | `question`, `customer-reported` |
| [Running `azd pipeline config --provider github` does not trigger actions on Codespaces](https://github.com/Azure/azure-dev/issues/5421) | #5421 | 2025-07-01 | `bug`, `codespaces`, `pipelines` |
| [[Issue] Configurting a KeyVault secret breaks the bicep provider when provisioning the infrastructure](https://github.com/Azure/azure-dev/issues/5211) | #5211 | 2025-05-16 | `question`, `customer-reported`, `aspire` |
| [[Issue] AKS service target deploys both Helm charts and manifests even when using Helm exclusively](https://github.com/Azure/azure-dev/issues/5191) | #5191 | 2025-05-13 | `aks` |
| [[Issue] Still Unable to deploy to AKS cluster with Microsoft Entra ID authentication and Azure RBAC enabled](https://github.com/Azure/azure-dev/issues/5181) | #5181 | 2025-05-11 | `aks` |
| [[Issue] Anonymous volume mounts in Aspire cause deployment breaks](https://github.com/Azure/azure-dev/issues/5058) | #5058 | 2025-04-08 | `aspire` |
| [Issue for `Helm for AKS`](https://github.com/Azure/azure-dev/issues/4863) | #4863 | 2025-02-28 | `aks` |
| [compose: add key Azure services post Beta](https://github.com/Azure/azure-dev/issues/4579) | #4579 | 2024-11-21 | `compose` |
| [compose: spec - database to managed identity](https://github.com/Azure/azure-dev/issues/4481) | #4481 | 2024-10-23 | `design`, `compose` |
| [Fail to load api page after `azd up` for `todo-nodejs-mongo-aks`](https://github.com/Azure/azure-dev/issues/4459) | #4459 | 2024-10-18 | `templates`, `aks`, `needs-triage` |
| [Analysis of GitHub issues by tag](https://github.com/Azure/azure-dev/issues/4445) | #4445 | 2024-10-16 | `pm` |
| [define: naming for `azure.yaml` project and services](https://github.com/Azure/azure-dev/issues/4400) | #4400 | 2024-10-02 | `enhancement` |
| [Fail to run `azd pipeline config --provider azdo` for `todo-nodejs-mongo-aks`](https://github.com/Azure/azure-dev/issues/4348) | #4348 | 2024-09-19 | `bug`, `templates`, `azdo`, `pipelines` |
| [[Issue] azd up or deploy hangs when Docker Desktop is outdated without any feedback](https://github.com/Azure/azure-dev/issues/4045) | #4045 | 2024-06-28 | `error handling`, `aca`, `macOS - arm64` |
| [Getting Started UX Improvements](https://github.com/Azure/azure-dev/issues/4032) | #4032 | 2024-06-21 | `pm`, `user-study`, `ux improvements`, `ux impact` |
| [[Issue] Helm deployment namespace conflict](https://github.com/Azure/azure-dev/issues/3673) | #3673 | 2024-04-09 | `enhancement`, `aks` |
| [[Issue] Changing the `name` property did not deploy to new namespace](https://github.com/Azure/azure-dev/issues/3590) | #3590 | 2024-03-25 | `bug`, `aks` |
| [[Issue] Angular 17 deployment to SWA breaks after upgrade because output path default changes and requires manual reconfig](https://github.com/Azure/azure-dev/issues/3414) | #3414 | 2024-02-21 | `enhancement`, `swa` |
| [Create public documentation for developer expectations when using each supported service target or language](https://github.com/Azure/azure-dev/issues/3363) | #3363 | 2024-02-14 | `documentation` |
| [[Issue] host: aks fails on postprovision hook if iac doesn't include aks](https://github.com/Azure/azure-dev/issues/3272) | #3272 | 2024-02-01 | `aks`, `extensibility` |
| [Support to reference multiple container projects](https://github.com/Azure/azure-dev/issues/3236) | #3236 | 2024-01-27 | `aks`, `aca` |
| [[Spike] improve azure container app deployments to avoid error-prone and confusing multiple revisions](https://github.com/Azure/azure-dev/issues/3116) | #3116 | 2023-12-13 | `question`, `customer-reported`, `needs-team-attention`, `aca` |
| [[Issue]: kubeconfig handling makes github workflow kubectl commands incompatible](https://github.com/Azure/azure-dev/issues/2481) | #2481 | 2023-07-05 | `enhancement`, `question`, `aks`, `customer-reported` |

### Multi-tenant Authentication

**Total Open Issues:** 19

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template parameters](https://github.com/Azure/azure-dev/issues/5507) | #5507 | 2025-07-20 | `question`, `customer-reported` |
| [Implement automatic tagging policy engine](https://github.com/Azure/azure-dev/issues/5327) | #5327 | 2025-06-16 | `none` |
| [Design environment-specific naming convention system](https://github.com/Azure/azure-dev/issues/5326) | #5326 | 2025-06-16 | `none` |
| [Design environment type configuration schema](https://github.com/Azure/azure-dev/issues/5313) | #5313 | 2025-06-16 | `none` |
| [Environment Type System](https://github.com/Azure/azure-dev/issues/5311) | #5311 | 2025-06-16 | `none` |
| [Improve the experience for `pipeline config` for Tenants where applicationServiceManagementReference is mandatory](https://github.com/Azure/azure-dev/issues/5221) | #5221 | 2025-05-27 | `pipelines` |
| [[Issue] Still Unable to deploy to AKS cluster with Microsoft Entra ID authentication and Azure RBAC enabled](https://github.com/Azure/azure-dev/issues/5181) | #5181 | 2025-05-11 | `aks` |
| [Remote state does not work when user has multiple tenants.](https://github.com/Azure/azure-dev/issues/4903) | #4903 | 2025-03-06 | `remote-env` |
| [`azd` in DevCenter mode does not return all project/environments](https://github.com/Azure/azure-dev/issues/4798) | #4798 | 2025-02-14 | `bug` |
| [[Issue] Security Policies prevent azd from executing correctly.](https://github.com/Azure/azure-dev/issues/4737) | #4737 | 2025-01-28 | `question`, `customer-reported`, `aspire` |
| [Unable to run tenant level deployments](https://github.com/Azure/azure-dev/issues/4643) | #4643 | 2024-12-20 | `Bicep`, `core` |
| [Support resource picker for parameters](https://github.com/Azure/azure-dev/issues/4530) | #4530 | 2024-11-08 | `feature` |
| [compose: spec - database to managed identity](https://github.com/Azure/azure-dev/issues/4481) | #4481 | 2024-10-23 | `design`, `compose` |
| [[pipeline config] Add one-time confirmation for the remote](https://github.com/Azure/azure-dev/issues/4197) | #4197 | 2024-08-09 | `enhancement`, `pipelines` |
| [azd package fails after installing buildx](https://github.com/Azure/azure-dev/issues/3807) | #3807 | 2024-04-27 | `command`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [[Issue] Enable azure.yaml to specify optional deployments for services](https://github.com/Azure/azure-dev/issues/3514) | #3514 | 2024-03-08 | `feature`, `core` |
| [[Issue] Deploy failed to SWA with Still in WaitingForDeployment state](https://github.com/Azure/azure-dev/issues/3074) | #3074 | 2023-12-06 | `bug`, `command`, `question`, `customer-reported`, `core` |
| [[Issue] AzDO hosted images do not have setup-azd pre-installed](https://github.com/Azure/azure-dev/issues/3030) | #3030 | 2023-11-28 | `enhancement`, `azdo`, `pipelines` |
| [[Issue] Specify azure.yaml for azd up](https://github.com/Azure/azure-dev/issues/2736) | #2736 | 2023-09-12 | `feature`, `core` |

### Token Management

**Total Open Issues:** 15

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template parameters](https://github.com/Azure/azure-dev/issues/5507) | #5507 | 2025-07-20 | `question`, `customer-reported` |
| [[Issue]`azd pipleline config` didnt work - struggled with gh cli bootstrapping](https://github.com/Azure/azure-dev/issues/5431) | #5431 | 2025-07-03 | `pipelines`, `no-recent-activity`, `needs-author-feedback` |
| [SPIKE: determine LLM access options for azd](https://github.com/Azure/azure-dev/issues/5375) | #5375 | 2025-06-18 | `none` |
| [azd env refresh bring "old" resources back in the .env file](https://github.com/Azure/azure-dev/issues/5106) | #5106 | 2025-04-21 | `question`, `customer-reported` |
| [compose: static site support](https://github.com/Azure/azure-dev/issues/5094) | #5094 | 2025-04-17 | `compose` |
| [compose: provisioned resource(s) naming](https://github.com/Azure/azure-dev/issues/4915) | #4915 | 2025-03-08 | `compose` |
| [compose: spec - database to managed identity](https://github.com/Azure/azure-dev/issues/4481) | #4481 | 2024-10-23 | `design`, `compose` |
| [[Document] What does `azd env refresh` actually do?](https://github.com/Azure/azure-dev/issues/4368) | #4368 | 2024-09-23 | `documentation` |
| [[AspireDeployment] Initializing an Aspire project without 'Subscription', 'Location' will send an incorrect Prompt request on RefreshEnvironment](https://github.com/Azure/azure-dev/issues/3953) | #3953 | 2024-05-24 | `question`, `vs`, `customer-reported`, `aspire` |
| [dotnet/eShop certificate/login issue](https://github.com/Azure/azure-dev/issues/3791) | #3791 | 2024-04-25 | `question`, `customer-reported`, `needs-team-attention`, `aspire` |
| [When running `azd env <INVALID_CMD>`, azd doesn't call out the invalid command error](https://github.com/Azure/azure-dev/issues/3662) | #3662 | 2024-04-08 | `command` |
| [Obtaining subscription-level deployment state is slow](https://github.com/Azure/azure-dev/issues/3577) | #3577 | 2024-03-22 | `performance` |
| [Deployment iteration ID as environment variable](https://github.com/Azure/azure-dev/issues/3180) | #3180 | 2024-01-07 | `enhancement`, `question`, `customer-reported`, `core` |
| [[Issue] Deploy failed to SWA with Still in WaitingForDeployment state](https://github.com/Azure/azure-dev/issues/3074) | #3074 | 2023-12-06 | `bug`, `command`, `question`, `customer-reported`, `core` |
| [Add subscription/region selection to `azd env refresh`?](https://github.com/Azure/azure-dev/issues/2415) | #2415 | 2023-06-14 | `discuss`, `hacktoberfest` |

### WSL/Linux Authentication

**Total Open Issues:** 14

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Broken .NET Aspire Azure CI/CD pipeline: error unmarshalling Bicep template parameters](https://github.com/Azure/azure-dev/issues/5507) | #5507 | 2025-07-20 | `question`, `customer-reported` |
| [Fail to run `azd pipeline config` for terraform templates](https://github.com/Azure/azure-dev/issues/5422) | #5422 | 2025-07-01 | `none` |
| [[Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in Azure DevOps with WIF, Despite principalId Configuration](https://github.com/Azure/azure-dev/issues/5201) | #5201 | 2025-05-15 | `question`, `pipelines`, `customer-reported`, `aspire` |
| [[Issue] Filtering not working as expected](https://github.com/Azure/azure-dev/issues/5127) | #5127 | 2025-04-28 | `command`, `templates` |
| [compose: App Service - containerless/runtime-specific support](https://github.com/Azure/azure-dev/issues/5050) | #5050 | 2025-04-07 | `compose` |
| [Fail to run `azd pipeline config --provider github` and `azd pipeline config --provider azdo`](https://github.com/Azure/azure-dev/issues/4347) | #4347 | 2024-09-19 | `terraform`, `pipelines` |
| [[Issue] Remote end - `InvalidAuthenticationInfo`](https://github.com/Azure/azure-dev/issues/3808) | #3808 | 2024-04-28 | `question`, `terraform`, `customer-reported`, `needs-team-attention`, `remote-env` |
| [azd package fails after installing buildx](https://github.com/Azure/azure-dev/issues/3807) | #3807 | 2024-04-27 | `command`, `question`, `customer-reported`, `needs-team-attention`, `core` |
| [[Issue] azd not installed correctly on mac m1 dev container for ](https://github.com/Azure/azure-dev/issues/3707) | #3707 | 2024-04-13 | `bug`, `engsys`, `question`, `installer`, `customer-reported`, `needs-team-attention` |
| [[Issue/enhancement] Cross-platform shell commands behavior](https://github.com/Azure/azure-dev/issues/3613) | #3613 | 2024-03-28 | `enhancement`, `extensibility`, `hooks` |
| [AZD hangs in WSL2 when running init --template](https://github.com/Azure/azure-dev/issues/3583) | #3583 | 2024-03-23 | `bug`, `templates`, `wsl` |
| [Obtaining subscription-level deployment state is slow](https://github.com/Azure/azure-dev/issues/3577) | #3577 | 2024-03-22 | `performance` |
| [[Issue] Function App Deploy: Inconsistent on Consumption vs. Premium Plan](https://github.com/Azure/azure-dev/issues/3209) | #3209 | 2024-01-19 | `functions` |
| [[Issue] Deploy failed to SWA with Still in WaitingForDeployment state](https://github.com/Azure/azure-dev/issues/3074) | #3074 | 2023-12-06 | `bug`, `command`, `question`, `customer-reported`, `core` |

### Device Code Flow

**Total Open Issues:** 8

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [[Issue]`azd pipleline config` didnt work - struggled with gh cli bootstrapping](https://github.com/Azure/azure-dev/issues/5431) | #5431 | 2025-07-03 | `pipelines`, `no-recent-activity`, `needs-author-feedback` |
| [[Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in Azure DevOps with WIF, Despite principalId Configuration](https://github.com/Azure/azure-dev/issues/5201) | #5201 | 2025-05-15 | `question`, `pipelines`, `customer-reported`, `aspire` |
| [compose: static site support](https://github.com/Azure/azure-dev/issues/5094) | #5094 | 2025-04-17 | `compose` |
| [Can not display option and select option when run `azd init` by GoLand](https://github.com/Azure/azure-dev/issues/4311) | #4311 | 2024-09-12 | `enhancement`, `needs-team-attention` |
| [dotnet/eShop certificate/login issue](https://github.com/Azure/azure-dev/issues/3791) | #3791 | 2024-04-25 | `question`, `customer-reported`, `needs-team-attention`, `aspire` |
| [[Issue] --use-device-code auth flow presents the wrong app name](https://github.com/Azure/azure-dev/issues/3742) | #3742 | 2024-04-18 | `cli`, `core` |
| [When running `azd env <INVALID_CMD>`, azd doesn't call out the invalid command error](https://github.com/Azure/azure-dev/issues/3662) | #3662 | 2024-04-08 | `command` |
| [[Issue] Angular 17 deployment to SWA breaks after upgrade because output path default changes and requires manual reconfig](https://github.com/Azure/azure-dev/issues/3414) | #3414 | 2024-02-21 | `enhancement`, `swa` |

### SAML/SSO

**Total Open Issues:** 7

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Design scale unit configuration schema](https://github.com/Azure/azure-dev/issues/5303) | #5303 | 2025-06-16 | `none` |
| [Scale Units and Multi-Region Support](https://github.com/Azure/azure-dev/issues/5302) | #5302 | 2025-06-16 | `feature` |
| [Australia Southeast Aspire Dashboard failing](https://github.com/Azure/azure-dev/issues/5150) | #5150 | 2025-05-02 | `question`, `customer-reported` |
| [compose: explicit mapping](https://github.com/Azure/azure-dev/issues/4747) | #4747 | 2025-01-31 | `design`, `compose` |
| [define: naming for `azure.yaml` project and services](https://github.com/Azure/azure-dev/issues/4400) | #4400 | 2024-10-02 | `enhancement` |
| [Expose OneAuth Authentication on Windows as an Alpha Feature.](https://github.com/Azure/azure-dev/issues/3431) | #3431 | 2024-02-23 | `enhancement`, `authn` |
| [azd pipeline config service principal cleanup](https://github.com/Azure/azure-dev/issues/2431) | #2431 | 2023-06-16 | `engsys` |

### Service Principal Authentication

**Total Open Issues:** 7

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [Improve the experience for `pipeline config` for Tenants where applicationServiceManagementReference is mandatory](https://github.com/Azure/azure-dev/issues/5221) | #5221 | 2025-05-27 | `pipelines` |
| [[Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in Azure DevOps with WIF, Despite principalId Configuration](https://github.com/Azure/azure-dev/issues/5201) | #5201 | 2025-05-15 | `question`, `pipelines`, `customer-reported`, `aspire` |
| [Missing Documentation on Remote Builds for Docker Image w/ ACR](https://github.com/Azure/azure-dev/issues/5156) | #5156 | 2025-05-05 | `documentation` |
| [Let azd to ignore auth for the SP with a flag when running pipeline config](https://github.com/Azure/azure-dev/issues/4128) | #4128 | 2024-07-16 | `enhancement`, `pipelines` |
| [[Issue] azd pipeline config - questions for documentation](https://github.com/Azure/azure-dev/issues/3055) | #3055 | 2023-12-03 | `enhancement`, `question`, `pipelines`, `customer-reported` |
| [Add variables as "scaffolding" should `azd pipeline config` fail...](https://github.com/Azure/azure-dev/issues/2816) | #2816 | 2023-10-03 | `feature`, `pipelines` |
| [azd pipeline config service principal cleanup](https://github.com/Azure/azure-dev/issues/2431) | #2431 | 2023-06-16 | `engsys` |

### Federated Identity

**Total Open Issues:** 5

| Issue | Number | Created | Labels |
|-------|---------|---------|--------|
| [azd login with federated credential fails because the subject is scoped to the GitHub environment name](https://github.com/Azure/azure-dev/issues/5473) | #5473 | 2025-07-10 | `question` |
| [[Issue]`azd pipleline config` didnt work - struggled with gh cli bootstrapping](https://github.com/Azure/azure-dev/issues/5431) | #5431 | 2025-07-03 | `pipelines`, `no-recent-activity`, `needs-author-feedback` |
| [[Issue] azd Continues to Make /me Graph API Call and Prompts for Parameters in Azure DevOps with WIF, Despite principalId Configuration](https://github.com/Azure/azure-dev/issues/5201) | #5201 | 2025-05-15 | `question`, `pipelines`, `customer-reported`, `aspire` |
| [Feature request: azd pipeline config --provider azdo -> to re-use existing service connection](https://github.com/Azure/azure-dev/issues/4138) | #4138 | 2024-07-22 | `enhancement`, `question`, `azdo`, `pipelines`, `customer-reported`, `needs-team-attention` |
| [Let azd to ignore auth for the SP with a flag when running pipeline config](https://github.com/Azure/azure-dev/issues/4128) | #4128 | 2024-07-16 | `enhancement`, `pipelines` |
