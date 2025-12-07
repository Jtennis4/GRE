# Sociology Paper Analyzer

A comprehensive Python tool for analyzing sociology research papers. This analyzer extracts key information including research methodologies, theoretical frameworks, sociological concepts, citations, and provides detailed statistical analysis.

## Features

### 1. **Document Statistics**
- Word count, sentence count, and paragraph count
- Average sentence length calculation
- Overall document structure analysis

### 2. **Research Methodology Detection**
Automatically identifies and quantifies:
- **Qualitative methods**: ethnography, interviews, focus groups, case studies, participant observation, grounded theory, discourse analysis, etc.
- **Quantitative methods**: surveys, statistical analysis, regression, ANOVA, correlations, t-tests, etc.
- **Mixed methods**: triangulation, sequential/concurrent designs

### 3. **Sociological Theory Identification**
Detects mentions of major theoretical frameworks:
- Structural Functionalism (Parsons, Merton, Durkheim)
- Conflict Theory (Marx, class conflict, power dynamics)
- Symbolic Interactionism (Goffman, Blumer, Mead)
- Feminist Theory (patriarchy, gender inequality, intersectionality)
- Critical Race Theory (racial formation, systemic racism)
- Postmodernism (Foucault, Derrida, discourse analysis)
- Rational Choice Theory (cost-benefit analysis, exchange theory)
- Social Constructionism (Berger & Luckmann)

### 4. **Key Concept Extraction**
Identifies important sociological concepts:
- Social capital, cultural capital, habitus
- Stigma, deviance, anomie
- Social solidarity, stratification, socialization
- Norms, values, roles, status
- Social movements, collective behavior, social change
- And many more...

### 5. **Research Component Analysis**
Extracts and counts:
- Research questions and hypotheses
- Sample size indicators
- Findings and results statements
- Limitations and caveats
- Future research suggestions

### 6. **Citation Analysis**
- Total citation count
- Unique citation identification
- Citation format detection (APA style)
- Sample citations for review

### 7. **Keyword Extraction**
- Top 15-20 most frequent keywords
- Automatic stop-word filtering
- Frequency-based ranking

## Installation

### Basic Installation (No Dependencies)
The analyzer works with plain text files using Python's standard library only:

```bash
# No additional installation needed
python3 sociology_paper_analyzer.py your_paper.txt
```

### Optional: PDF Support
To analyze PDF files, install optional dependencies:

```bash
pip install PyPDF2 pdfplumber
```

### Optional: Advanced NLP
For more sophisticated analysis:

```bash
pip install nltk spacy
```

## Usage

### Basic Analysis
```bash
python3 sociology_paper_analyzer.py paper.txt
```

### Export Results to JSON
```bash
python3 sociology_paper_analyzer.py paper.txt --export analysis_results.json
```

### Command Line Options
- `<file_path>`: Path to the paper file (required)
- `--export <output.json>`: Export results to JSON file (optional)

## Input File Formats

### Supported Formats
- **.txt**: Plain text files (fully supported)
- **.md**: Markdown files (fully supported)
- **.pdf**: PDF files (requires PyPDF2 or pdfplumber)

### Preparing Your Paper
For best results:
1. Convert your paper to plain text (.txt) format
2. Ensure proper encoding (UTF-8 recommended)
3. Remove headers, footers, and page numbers if possible
4. Keep the main text content intact

## Example Output

```
======================================================================
SOCIOLOGY PAPER ANALYZER
======================================================================

Analyzing: example_paper.txt
Analysis Date: 2025-12-07 10:30:00

======================================================================
1. DOCUMENT STATISTICS
======================================================================
Word Count: 8,542
Sentence Count: 342
Average Sentence Length: 25.0 words
Paragraph Count: 87

======================================================================
2. RESEARCH METHODOLOGY
======================================================================
Qualitative: 45 mentions (62.5%)
Quantitative: 20 mentions (27.8%)
Mixed Methods: 7 mentions (9.7%)

Primary Methodology: Qualitative

======================================================================
3. SOCIOLOGICAL THEORIES
======================================================================

Symbolic Interactionism:
  Mentions: 23
  Related terms: goffman, dramaturgy, impression management

Feminist Theory:
  Mentions: 15
  Related terms: feminist, gender inequality, patriarchy

======================================================================
4. KEY SOCIOLOGICAL CONCEPTS
======================================================================
1. Social Capital: 12 mentions
2. Stigma: 9 mentions
3. Socialization: 8 mentions
...

======================================================================
5. RESEARCH COMPONENTS
======================================================================
Research Question: 3 mentions
Hypothesis: 2 mentions
Findings: 18 mentions
Limitations: 4 mentions

======================================================================
6. CITATION ANALYSIS
======================================================================
Total Citations Found: 87
Unique Citations: 65

Sample Citations:
  - (Goffman, 1959)
  - (Bourdieu, 1986)
  - (Collins et al., 2018)
...

======================================================================
7. TOP KEYWORDS
======================================================================
1. social: 145 occurrences
2. gender: 89 occurrences
3. identity: 76 occurrences
...
```

## Use Cases

### For Students
- Analyze your own papers to ensure balanced theoretical coverage
- Identify gaps in methodology or theoretical framework
- Check citation density and diversity
- Extract key themes for revision

### For Researchers
- Quick overview of paper content and focus
- Methodology verification
- Theoretical framework assessment
- Comparative analysis across multiple papers

### For Educators
- Assess student papers systematically
- Provide detailed feedback on theoretical engagement
- Track methodology usage across assignments
- Identify common themes in student work

## Customization

The analyzer can be customized by editing the `sociology_paper_analyzer.py` file:

### Add New Theories
```python
self.theories['your_theory'] = [
    'keyword1', 'keyword2', 'key phrase'
]
```

### Add New Concepts
```python
self.concepts.extend([
    'new concept', 'another concept'
])
```

### Modify Methodology Keywords
```python
self.methodologies['qualitative'].extend([
    'new method', 'another approach'
])
```

## Tips for Best Results

1. **Clean Text**: Remove extraneous content (headers, footers, page numbers)
2. **Complete Papers**: Analysis is most accurate on complete papers with full content
3. **Academic Writing**: Optimized for formal academic sociology papers
4. **Multiple Runs**: Analyze multiple drafts to track improvements
5. **JSON Export**: Use `--export` for programmatic analysis of results

## Limitations

- Text-based analysis only (cannot interpret images, tables, or charts)
- Pattern matching approach (may miss contextual nuances)
- English language optimized
- Requires properly formatted text input
- Citation detection works best with APA format

## Future Enhancements

Potential future features:
- PDF direct support
- Sentiment analysis
- Network analysis of cited authors
- Comparative analysis across multiple papers
- Machine learning-based classification
- Interactive web interface
- Export to multiple formats (CSV, HTML, PDF reports)

## Contributing

Suggestions and improvements are welcome! Key areas for contribution:
- Additional sociological theories
- More methodology keywords
- Enhanced citation parsing
- Support for additional file formats
- Improved keyword extraction

## License

This tool is provided as-is for educational and research purposes.

## Support

For issues, suggestions, or questions:
1. Check this README for usage instructions
2. Review example outputs
3. Verify input file format and encoding
4. Test with the provided example files

---

**Version**: 1.0.0
**Last Updated**: December 2025
**Author**: Sociology Paper Analyzer Project
