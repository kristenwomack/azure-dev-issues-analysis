# Query Runner Tools - Usage Guide

This directory contains scripts and tools for collecting GitHub issues data from the Azure/azure-dev repository for comprehensive analysis.

## Quick Start

### Basic System Test

Before running the full analysis, you can verify the system with a simple hello world test:

```bash
cd tools
python hello_test.py
```

This will verify that Python and basic dependencies are working correctly.

### Option 1: Python Script (Recommended)

1. **Setup Environment**:
   ```bash
   cd tools
   pip install -r requirements.txt
   ```

2. **Get GitHub Token**:
   - Visit https://github.com/settings/tokens
   - Create a new token with `repo` and `read:org` permissions
   - Copy the token

3. **Run Analysis**:
   ```bash
   python run_queries.py --token YOUR_GITHUB_TOKEN
   ```

### Option 2: Shell Script (GitHub CLI)

1. **Install GitHub CLI**:
   ```bash
   # On macOS
   brew install gh
   
   # On Windows
   winget install GitHub.cli
   
   # On Linux
   sudo apt install gh
   ```

2. **Authenticate**:
   ```bash
   gh auth login
   ```

3. **Run Analysis**:
   ```bash
   chmod +x run_queries.sh
   ./run_queries.sh
   ```

## Script Options

### Python Script (`run_queries.py`)

```bash
# Basic usage
python run_queries.py --token YOUR_TOKEN

# Custom output directory
python run_queries.py --token YOUR_TOKEN --output-dir ./custom-output

# Include detailed data enrichment (slower)
python run_queries.py --token YOUR_TOKEN --enrich

# Different repository
python run_queries.py --token YOUR_TOKEN --repo-owner Microsoft --repo-name vscode
```

### Shell Script (`run_queries.sh`)

```bash
# Basic usage
./run_queries.sh

# Custom repository
./run_queries.sh --repo Microsoft/vscode

# Custom output directory
./run_queries.sh --output-dir ./custom-output
```

## Output Structure

After running, you'll get the following directory structure:

```
data/raw-data/
├── core/                          # Core issue queries
│   ├── high_engagement_*.json
│   ├── feature_requests_*.json
│   └── ...
├── category/                      # Category-specific queries
│   ├── auth_issues_*.json
│   ├── deployment_issues_*.json
│   └── ...
├── temporal/                      # Time-based analysis
│   ├── q1_2024_*.json
│   ├── recently_closed_*.json
│   └── ...
├── engagement/                    # Engagement metrics
│   ├── most_commented_*.json
│   └── ...
└── combined/                      # Aggregated results
    ├── all_queries_*.json         # All results combined
    ├── summary_*.csv              # Summary spreadsheet
    └── analysis_report_*.md       # Analysis report
```

## Understanding the Results

### JSON Files
- Each query result is saved as a separate JSON file
- Contains complete GitHub issue data including metadata, reactions, labels
- Use for detailed programmatic analysis

### CSV Summary
- `summary_*.csv` contains key metrics for all issues across all queries
- Columns: query_source, number, title, state, dates, labels, reactions, etc.
- Perfect for Excel analysis or quick filtering

### Analysis Report
- `analysis_report_*.md` provides an overview of what was collected
- Shows issue counts per query category
- Lists all generated files

## Query Categories

### Core Queries
- **High Engagement**: Issues with >5 reactions
- **Feature Requests**: Open enhancement issues
- **High Impact Bugs**: Bugs with >3 reactions
- **Recent Priority**: Recent issues with >2 reactions

### Category-Specific
- **Authentication**: Login and auth-related issues
- **Environment**: Environment management problems
- **Templates**: Template and scaffolding issues
- **Documentation**: Documentation gaps and requests
- **VS Code**: Extension integration issues
- **Deployment**: Deployment and provisioning failures
- **Installation**: Setup and installation problems
- **Containers**: Docker and container issues
- **Azure Integration**: Azure service integration problems

### Temporal Analysis
- **Quarterly Trends**: Issues by quarter (2024-2025)
- **Recent Activity**: Recently closed issues
- **Long-standing**: Old open issues

### Engagement Analysis
- **Most Commented**: Issues with >10 comments
- **Most Reacted**: Issues with >10 reactions
- **Recently Updated**: Recently active discussions

## Rate Limiting

Both scripts implement rate limiting to respect GitHub's API limits:

- **GitHub API**: 5,000 requests/hour for authenticated users
- **Search API**: 30 requests/minute
- Scripts use conservative limits with delays between requests

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   ```
   Error: Not authenticated with GitHub CLI
   ```
   **Solution**: Run `gh auth login` for shell script or check your token for Python script

2. **Rate Limit Exceeded**
   ```
   Error: API rate limit exceeded
   ```
   **Solution**: Wait an hour or use a different GitHub account

3. **No Results**
   ```
   Warning: Query failed or returned no results
   ```
   **Solution**: Check if the repository name is correct and public

4. **Permission Denied**
   ```
   Error: Resource not accessible by integration
   ```
   **Solution**: Ensure your GitHub token has `repo` permissions

### Performance Tips

1. **Start Small**: Test with a single query category first
2. **Use Filters**: Modify queries to focus on specific time periods
3. **Avoid Enrichment**: Skip `--enrich` option for faster collection
4. **Monitor Progress**: Both scripts show progress and can be interrupted safely

## Configuration

### Python Script Configuration
Copy `config_template.yaml` to `config.yaml` and customize:

```yaml
github:
  token: "your_token_here"
  repository:
    owner: "Azure"
    name: "azure-dev"

output:
  directory: "./data/raw-data"
  include_enriched_data: false
```

Then run:
```bash
python run_queries.py --config config.yaml
```

### Environment Variables
Both scripts support environment variables:

```bash
export GITHUB_TOKEN="your_token_here"
export GITHUB_REPO="Azure/azure-dev"
export OUTPUT_DIR="./data/raw-data"
```

## Next Steps

After collecting the data:

1. **Review Summary**: Start with the CSV summary file
2. **Follow Analysis Templates**: Use the frameworks in `../analysis/` directory
3. **Generate Insights**: Look for patterns in high-engagement issues
4. **Create Reports**: Use `../reports/` templates for stakeholder communication

## Testing and Validation

### Basic System Tests

The tools directory includes several test utilities:

- **`hello_test.py`**: Basic system verification and hello world test
- **`test_hello.py`**: Unit tests for the hello world functionality
- **`test_auth.py`**: GitHub authentication testing
- **`simple_test.py`**: Simple GitHub API access test

Run tests to verify your setup:

```bash
# Basic system test
python hello_test.py

# Run unit tests
python test_hello.py

# Test GitHub authentication (requires GITHUB_TOKEN)
python test_auth.py

# Test GitHub API access
python simple_test.py
```

## Advanced Usage

### Custom Queries
Modify the scripts to add your own search queries:

```python
# In run_queries.py, add to run_category_queries():
custom_results = self.search_issues('your custom search terms')
```

### Data Processing
The JSON output can be processed with additional tools:

```bash
# Count issues by label
jq '[.[] | .labels[].name] | group_by(.) | map({label: .[0], count: length})' data.json

# Find issues with most reactions
jq 'sort_by(.reactions.total_count) | reverse | .[0:10]' data.json
```

### Integration
Results can be imported into analysis tools:
- **Python**: pandas, matplotlib for analysis
- **R**: ggplot2 for visualization  
- **Excel**: Direct CSV import
- **Tableau**: JSON connector for dashboards

---

*These tools support the comprehensive GitHub issues analysis outlined in [Issue #4445](https://github.com/Azure/azure-dev/issues/4445).*
