# Analysis Results

This folder contains the actual analysis results and raw data insights generated using the frameworks defined in the `/prompts` directory. These analyses serve as the foundation for the polished reports in the `/reports` directory.

## Purpose

The analysis files in this folder should contain concrete data, findings, and insights about Azure Developer CLI issues. Each analysis should follow the corresponding framework template from the `/prompts/analysis-frameworks` directory and focus on raw data, metrics, and initial findings that will later be synthesized into customer-facing reports.

## File Organization

### Expected Files

1. **Top Customer Issues Analysis**
   - Following the framework in `/prompts/analysis-frameworks/customer-issues.md`
   - Contains actual issue data, metrics, and findings
   - Updated periodically with new data

2. **Issue Clustering Analysis**
   - Following the framework in `/prompts/analysis-frameworks/issue-clustering.md`
   - Contains identified issue clusters and patterns
   - Updated as new patterns emerge

3. **Feature Gap Analysis**
   - Following the framework in `/prompts/analysis-frameworks/feature-gaps.md`
   - Contains actual feature comparisons and gap findings
   - Updated with each major release or feature addition

## File Naming Convention

- Use date prefixes for periodic analyses: `YYYYMMDD-analysis-name.md`
- Use clear, descriptive names that indicate the type of analysis
- Include version numbers if analyzing specific releases

## Update Frequency

- Customer Issues Analysis: Monthly
- Issue Clustering Analysis: Quarterly
- Feature Gap Analysis: With each major release
- Ad-hoc analyses: As needed

## Using the Templates

1. Copy the appropriate template from `/prompts/analysis-frameworks/`
2. Create a new file in this directory
3. Fill in the template with actual data and findings
4. Include the date and scope of analysis

## Related Resources

- Templates: `/prompts/templates/`
- Frameworks: `/prompts/analysis-frameworks/`
- Raw Data: `/data/`
- Tools: `/tools/`