# Customer Issues Analysis Framework

## Analysis Framework

**Goal**: Identify the most frequently reported problems and developer pain points in the Azure Developer CLI.

## Methodology

### Data Collection
- Retrieve all open and closed issues from Azure/azure-dev repository
- Categorize issues by type: bugs, feature requests, documentation gaps, usability issues
- Count engagement metrics: mentions, upvotes (👍 reactions), comments
- Analyze issue recency and frequency of reports

### Ranking Criteria
Issues will be ranked by:
1. **Total reactions** (👍, ❤️, 🚀, 👀)
2. **Number of comments**
3. **Number of duplicate/similar issues**
4. **Recency and frequency of reports**
5. **Impact assessment** (High/Medium/Low)

## Analysis Methods

### Issue Classification
1. **Priority Levels**
   - P0: Blocking/Critical
   - P1: Major Functionality Impact
   - P2: Significant Usability Issue
   - P3: Minor/Enhancement

2. **Impact Categories**
   - Development Velocity
   - User Experience
   - Security/Compliance
   - Integration/Interoperability

3. **User Segments**
   - Individual Developers
   - Development Teams
   - Enterprise Organizations
   - New Users vs. Experienced

## Analysis Template

### Top 10 Customer Issues

#### Issue #1: [Issue Title] - #[Issue Number]
- **Type**: Bug/Feature/Documentation
- **Reactions**: 👍 [count], ❤️ [count], � [count], 👀 [count]
- **Comments**: [count]
- **Status**: Open/Closed
- **Created**: [date]
- **Last Updated**: [date]
- **Summary**: [Brief description of the issue]
- **Impact**: High/Medium/Low
- **User Personas Affected**: [Individual developers/Teams/Enterprise/New users/etc.]
- **Workarounds Available**: Yes/No - [description if available]

#### Issue #2: [Issue Title] - #[Issue Number]
[Same template as above]

#### Issue #3: [Issue Title] - #[Issue Number]
[Same template as above]

[Continue for top 10 issues...]
```

## Category Analysis

### Bug Issues
- **Total Count**: [number]
- **Top Subcategories**:
  - Authentication/Login: [count]
  - Deployment Failures: [count]
  - Environment Management: [count]
  - Template Issues: [count]
  - VS Code Extension: [count]
  - Installation/Setup: [count]

### Feature Requests
- **Total Count**: [number]
- **Top Requested Features**:
  - [Feature 1]: [count] requests
  - [Feature 2]: [count] requests
  - [Feature 3]: [count] requests

### Documentation Issues
- **Total Count**: [number]
- **Common Gaps**:
  - Missing how-to guides: [count]
  - Unclear error messages: [count]
  - Missing examples: [count]

### Usability Issues
- **Total Count**: [number]
- **Common Complaints**:
  - Confusing workflow: [count]
  - Poor error messages: [count]
  - Missing feedback: [count]

## Impact Assessment

### High Impact Issues
Issues that:
- Block core functionality
- Affect many users (high engagement)
- Have no workarounds
- Impact new user onboarding

### Medium Impact Issues
Issues that:
- Affect specific workflows
- Have partial workarounds
- Impact user productivity

### Low Impact Issues
Issues that:
- Are edge cases
- Have clear workarounds
- Affect advanced use cases only

Remember: Focus on actionable insights that can drive improvements in the developer experience.