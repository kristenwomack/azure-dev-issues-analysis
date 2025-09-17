# Duplicate and Similar Issue Clustering

## Analysis Framework

**Goal**: Group related issues that may be addressing the same underlying problem to identify opportunities for consolidation and root cause resolution.

## Methodology

### Clustering Approach
- Identify issues with similar titles, descriptions, or error messages
- Look for common keywords, error codes, or workflows
- Group beyond existing GitHub labels using semantic similarity
- Consider issues that might be different symptoms of the same root cause

### Categories to Analyze

#### Authentication/Login Issues
- Login failures
- Token problems
- Permission errors
- Multi-tenant authentication

#### Environment Management Problems
- Environment switching
- Variable configuration
- State management
- Cleanup issues

#### Deployment Failures
- Infrastructure provisioning
- Service deployment
- Configuration errors
- Resource conflicts

#### Template/Scaffolding Issues
- Template initialization
- Customization problems
- Template updates
- Missing templates

#### CLI Installation/Setup Problems
- Installation failures
- Path issues
- Dependency conflicts
- Version mismatches

#### VS Code Extension Issues
- Extension activation
- Command failures
- Integration problems
- UI issues

#### Docker/Container Related Issues
- Container build failures
- Registry problems
- Image issues
- Container runtime errors

#### Azure Service Integration Problems
- Service connectivity
- API failures
- Configuration issues
- Resource management

## Analysis Template

### Issue Cluster #1: [Cluster Name] ([count] issues)

#### Primary Issue
- **Issue**: #[number] - [title]
- **Created**: [date]
- **Status**: [Open/Closed]
- **Reactions**: [count]
- **Comments**: [count]
- **Summary**: [description of main issue]

#### Related Issues
- **#[number]**: [brief title] - [similarity reason]
- **#[number]**: [brief title] - [similarity reason]
- **#[number]**: [brief title] - [similarity reason]

#### Common Patterns
- **Error Messages**: [common error patterns]
- **Keywords**: [recurring terms]
- **Workflows**: [common user scenarios]
- **Environment**: [common setup/configuration]

#### Root Cause Analysis
- **Likely Root Cause**: [analysis of underlying issue]
- **Contributing Factors**: [what makes this happen]
- **User Impact**: [how this affects users]

#### Suggested Consolidation
- **Recommended Primary Issue**: #[number]
- **Issues to Close as Duplicates**: #[list]
- **New Issue Needed**: Yes/No - [description if needed]
- **Action Required**: [specific steps to consolidate]

## Cluster Documentation

1. **Cluster Definition**
   - Clear category name
   - Scope description
   - Inclusion criteria
   - Exclusion criteria

2. **Pattern Description**
   - Common characteristics
   - Key identifiers
   - Related symptoms
   - Trigger conditions

3. **Impact Assessment**
   - User base affected
   - Workflow disruption
   - Business impact
   - Resolution urgency

## Cross-Reference Analysis

1. **Inter-Cluster Relationships**
   - Dependency patterns
   - Cause-effect chains
   - Common root causes
   - Shared solutions

2. **Version Correlation**
   - Feature dependencies
   - Breaking changes
   - Compatibility issues
   - Migration impacts

Remember: Focus on identifying systemic patterns that can lead to comprehensive solutions.