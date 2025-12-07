#!/usr/bin/env python3
"""
Sociology Paper Analyzer
A comprehensive tool for analyzing sociology research papers.
Extracts methodology, theories, concepts, themes, and provides detailed analysis.
"""

import re
import os
import sys
from collections import Counter
from datetime import datetime
import json

class SociologyPaperAnalyzer:
    """Main class for analyzing sociology papers."""

    def __init__(self):
        """Initialize the analyzer with sociology-specific patterns and keywords."""

        # Research methodologies
        self.methodologies = {
            'qualitative': [
                'ethnography', 'ethnographic', 'interview', 'focus group',
                'case study', 'participant observation', 'grounded theory',
                'narrative analysis', 'discourse analysis', 'content analysis',
                'phenomenology', 'phenomenological', 'autoethnography',
                'life history', 'oral history', 'fieldwork', 'field notes'
            ],
            'quantitative': [
                'survey', 'questionnaire', 'regression', 'statistical analysis',
                'anova', 'correlation', 'sample size', 'n =', 'p <', 'p-value',
                'significance', 't-test', 'chi-square', 'factor analysis',
                'logistic regression', 'descriptive statistics', 'inferential statistics',
                'random sample', 'probability sample', 'statistical significance'
            ],
            'mixed_methods': [
                'mixed method', 'mixed-method', 'triangulation',
                'sequential design', 'concurrent design', 'convergent design',
                'explanatory sequential', 'exploratory sequential'
            ]
        }

        # Major sociological theories
        self.theories = {
            'structural_functionalism': [
                'structural functionalism', 'functionalism', 'functional',
                'parsons', 'merton', 'durkheim', 'social structure',
                'social system', 'equilibrium', 'manifest function', 'latent function'
            ],
            'conflict_theory': [
                'conflict theory', 'marx', 'marxist', 'class conflict',
                'power dynamics', 'inequality', 'oppression', 'hegemony',
                'exploitation', 'domination', 'class struggle'
            ],
            'symbolic_interactionism': [
                'symbolic interaction', 'interactionism', 'goffman', 'blumer',
                'mead', 'dramaturgy', 'impression management', 'self concept',
                'looking glass self', 'significant other', 'generalized other'
            ],
            'feminist_theory': [
                'feminist', 'feminism', 'patriarchy', 'gender inequality',
                'intersectionality', 'womens studies', 'masculine', 'feminine',
                'gender roles', 'sex and gender', 'gender stratification'
            ],
            'critical_race_theory': [
                'critical race', 'crt', 'racial formation', 'systemic racism',
                'structural racism', 'racial inequality', 'colorblind',
                'white privilege', 'racialization'
            ],
            'postmodernism': [
                'postmodern', 'postmodernism', 'foucault', 'derrida',
                'deconstruction', 'discourse', 'power/knowledge',
                'grand narrative', 'metanarrative', 'fragmentation'
            ],
            'rational_choice': [
                'rational choice', 'rational actor', 'cost-benefit',
                'utility maximization', 'game theory', 'exchange theory',
                'social exchange'
            ],
            'social_constructionism': [
                'social construction', 'socially constructed', 'berger',
                'luckmann', 'reality construction', 'social reality'
            ]
        }

        # Key sociological concepts
        self.concepts = [
            'social capital', 'cultural capital', 'habitus', 'field',
            'stigma', 'deviance', 'anomie', 'social solidarity',
            'mechanical solidarity', 'organic solidarity',
            'gemeinschaft', 'gesellschaft', 'social mobility',
            'stratification', 'socialization', 'social control',
            'social institution', 'norms', 'values', 'roles',
            'status', 'achieved status', 'ascribed status',
            'in-group', 'out-group', 'reference group',
            'primary group', 'secondary group', 'bureaucracy',
            'rationalization', 'McDonaldization', 'globalization',
            'urbanization', 'modernization', 'secularization',
            'social movement', 'collective behavior', 'social change'
        ]

        # Research components
        self.research_patterns = {
            'hypothesis': r'(?:hypothesis|hypotheses|we hypothesize|hypothesized)',
            'research_question': r'(?:research question|RQ\d+|this study (?:asks|examines|investigates))',
            'sample': r'(?:sample size|n\s*=\s*\d+|participants?\s*\(n\s*=\s*\d+\))',
            'findings': r'(?:findings|results show|we found|discovered that|demonstrates? that)',
            'limitations': r'(?:limitation|caveat|shortcoming|weakness of this study)',
            'future_research': r'(?:future research|further investigation|future studies)'
        }

    def read_file(self, filepath):
        """Read text from file (supports .txt and basic text extraction)."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def detect_methodology(self, text):
        """Detect research methodology used in the paper."""
        text_lower = text.lower()
        methodology_scores = {
            'qualitative': 0,
            'quantitative': 0,
            'mixed_methods': 0
        }

        for method_type, keywords in self.methodologies.items():
            for keyword in keywords:
                methodology_scores[method_type] += len(re.findall(
                    r'\b' + re.escape(keyword) + r'\b',
                    text_lower
                ))

        return methodology_scores

    def identify_theories(self, text):
        """Identify sociological theories mentioned in the paper."""
        text_lower = text.lower()
        theories_found = {}

        for theory_name, keywords in self.theories.items():
            count = 0
            matched_terms = []
            for keyword in keywords:
                matches = len(re.findall(r'\b' + re.escape(keyword) + r'\b', text_lower))
                if matches > 0:
                    count += matches
                    matched_terms.append(keyword)

            if count > 0:
                theories_found[theory_name] = {
                    'count': count,
                    'terms': list(set(matched_terms))
                }

        return theories_found

    def extract_concepts(self, text):
        """Extract key sociological concepts from the paper."""
        text_lower = text.lower()
        concepts_found = {}

        for concept in self.concepts:
            count = len(re.findall(r'\b' + re.escape(concept) + r'\b', text_lower))
            if count > 0:
                concepts_found[concept] = count

        return dict(sorted(concepts_found.items(), key=lambda x: x[1], reverse=True))

    def analyze_research_components(self, text):
        """Analyze research components like hypotheses, research questions, etc."""
        components = {}

        for component, pattern in self.research_patterns.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            count = sum(1 for _ in matches)
            if count > 0:
                components[component] = count

        return components

    def extract_citations(self, text):
        """Extract and count citations in the paper."""
        # Common citation patterns
        patterns = [
            r'\([A-Z][a-z]+(?:,?\s+(?:and|&)\s+[A-Z][a-z]+)*,?\s+\d{4}\)',  # (Author, 2020)
            r'\([A-Z][a-z]+\s+et\s+al\.,?\s+\d{4}\)',  # (Author et al., 2020)
            r'[A-Z][a-z]+\s+\(\d{4}\)',  # Author (2020)
        ]

        all_citations = []
        for pattern in patterns:
            citations = re.findall(pattern, text)
            all_citations.extend(citations)

        return {
            'total_citations': len(all_citations),
            'unique_citations': len(set(all_citations)),
            'sample_citations': list(set(all_citations))[:10]
        }

    def extract_keywords(self, text, top_n=20):
        """Extract top keywords from the paper."""
        # Remove common words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
            'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
            'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
            'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both',
            'few', 'more', 'most', 'other', 'some', 'such', 'than', 'too', 'very'
        }

        # Extract words
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        words = [w for w in words if w not in stop_words]

        # Count frequencies
        word_freq = Counter(words)

        return word_freq.most_common(top_n)

    def generate_summary(self, text):
        """Generate a summary of the paper's characteristics."""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

        return {
            'word_count': len(text.split()),
            'sentence_count': len(sentences),
            'avg_sentence_length': len(text.split()) / max(len(sentences), 1),
            'paragraph_count': len(text.split('\n\n'))
        }

    def analyze(self, filepath):
        """Perform comprehensive analysis of a sociology paper."""
        print(f"\n{'='*70}")
        print(f"SOCIOLOGY PAPER ANALYZER")
        print(f"{'='*70}\n")
        print(f"Analyzing: {filepath}")
        print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Read the file
        text = self.read_file(filepath)
        if not text:
            return None

        # Perform analyses
        print(f"{'='*70}")
        print("1. DOCUMENT STATISTICS")
        print(f"{'='*70}")
        summary = self.generate_summary(text)
        print(f"Word Count: {summary['word_count']:,}")
        print(f"Sentence Count: {summary['sentence_count']:,}")
        print(f"Average Sentence Length: {summary['avg_sentence_length']:.1f} words")
        print(f"Paragraph Count: {summary['paragraph_count']:,}")

        print(f"\n{'='*70}")
        print("2. RESEARCH METHODOLOGY")
        print(f"{'='*70}")
        methodology = self.detect_methodology(text)
        total_method_mentions = sum(methodology.values())
        if total_method_mentions > 0:
            for method, count in sorted(methodology.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / total_method_mentions) * 100
                print(f"{method.replace('_', ' ').title()}: {count} mentions ({percentage:.1f}%)")

            # Determine primary methodology
            primary = max(methodology.items(), key=lambda x: x[1])
            if primary[1] > 0:
                print(f"\nPrimary Methodology: {primary[0].replace('_', ' ').title()}")
        else:
            print("No clear methodology indicators found.")

        print(f"\n{'='*70}")
        print("3. SOCIOLOGICAL THEORIES")
        print(f"{'='*70}")
        theories = self.identify_theories(text)
        if theories:
            for theory, data in sorted(theories.items(), key=lambda x: x[1]['count'], reverse=True):
                print(f"\n{theory.replace('_', ' ').title()}:")
                print(f"  Mentions: {data['count']}")
                print(f"  Related terms: {', '.join(data['terms'][:5])}")
        else:
            print("No major sociological theories explicitly identified.")

        print(f"\n{'='*70}")
        print("4. KEY SOCIOLOGICAL CONCEPTS")
        print(f"{'='*70}")
        concepts = self.extract_concepts(text)
        if concepts:
            for i, (concept, count) in enumerate(list(concepts.items())[:15], 1):
                print(f"{i}. {concept.title()}: {count} mentions")
        else:
            print("No standard sociological concepts identified.")

        print(f"\n{'='*70}")
        print("5. RESEARCH COMPONENTS")
        print(f"{'='*70}")
        components = self.analyze_research_components(text)
        if components:
            for component, count in components.items():
                print(f"{component.replace('_', ' ').title()}: {count} mentions")
        else:
            print("No clear research components identified.")

        print(f"\n{'='*70}")
        print("6. CITATION ANALYSIS")
        print(f"{'='*70}")
        citations = self.extract_citations(text)
        print(f"Total Citations Found: {citations['total_citations']}")
        print(f"Unique Citations: {citations['unique_citations']}")
        if citations['sample_citations']:
            print(f"\nSample Citations:")
            for cite in citations['sample_citations'][:5]:
                print(f"  - {cite}")

        print(f"\n{'='*70}")
        print("7. TOP KEYWORDS")
        print(f"{'='*70}")
        keywords = self.extract_keywords(text, top_n=15)
        for i, (word, count) in enumerate(keywords, 1):
            print(f"{i}. {word}: {count} occurrences")

        print(f"\n{'='*70}")
        print("ANALYSIS COMPLETE")
        print(f"{'='*70}\n")

        # Return structured results
        return {
            'filepath': filepath,
            'timestamp': datetime.now().isoformat(),
            'summary': summary,
            'methodology': methodology,
            'theories': theories,
            'concepts': concepts,
            'components': components,
            'citations': citations,
            'keywords': keywords
        }

    def export_results(self, results, output_file):
        """Export analysis results to a JSON file."""
        if results:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                print(f"Results exported to: {output_file}")
                return True
            except Exception as e:
                print(f"Error exporting results: {e}")
                return False
        return False


def main():
    """Main function to run the analyzer."""
    if len(sys.argv) < 2:
        print("Usage: python sociology_paper_analyzer.py <file_path> [--export output.json]")
        print("\nExample:")
        print("  python sociology_paper_analyzer.py paper.txt")
        print("  python sociology_paper_analyzer.py paper.txt --export analysis.json")
        sys.exit(1)

    filepath = sys.argv[1]

    # Check for export flag
    export_file = None
    if '--export' in sys.argv:
        export_index = sys.argv.index('--export')
        if len(sys.argv) > export_index + 1:
            export_file = sys.argv[export_index + 1]

    # Create analyzer and run analysis
    analyzer = SociologyPaperAnalyzer()
    results = analyzer.analyze(filepath)

    # Export if requested
    if export_file and results:
        analyzer.export_results(results, export_file)


if __name__ == "__main__":
    main()
