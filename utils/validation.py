"""Validate the paper extraction boundary before displaying model output."""
FIELDS = ('paper_name', 'title', 'authors', 'year', 'objective', 'research_problem',
          'methodology', 'sample', 'instrument', 'context_or_location', 'key_findings',
          'recommendations', 'limitations', 'keywords_from_paper', 'relevance_to_topic',
          'short_summary')

def validate_analysis(value, paper_name):
    if not isinstance(value, dict):
        raise ValueError('Paper analysis must be an object.')
    if set(value) != set(FIELDS):
        raise ValueError('Paper analysis has missing or unexpected fields.')
    if any(not isinstance(value[key], str) or not value[key].strip() for key in FIELDS):
        raise ValueError('Paper analysis fields must be nonempty text.')
    result = {key: value[key].strip() for key in FIELDS}
    result['paper_name'] = paper_name
    return result
