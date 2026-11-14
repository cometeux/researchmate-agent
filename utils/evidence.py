"""Validate cited excerpts. Exact quotation proves provenance, not entailment."""
import re

def normalize(text):
    return ' '.join(text.split())

def validate_answer(value, sources):
    if not isinstance(value, dict) or set(value) != {'claims'} or not isinstance(value['claims'], list):
        raise ValueError('Expected a claims list.')
    checked = []
    for claim in value['claims']:
        if not isinstance(claim, dict) or set(claim) != {'text', 'source_id', 'quote'}:
            raise ValueError('Invalid claim fields.')
        if any(not isinstance(claim[k], str) or not claim[k].strip() for k in claim):
            raise ValueError('Claim fields must be nonempty text.')
        match = re.fullmatch(r'S([1-9][0-9]*)', claim['source_id'])
        if not match or int(match[1]) > len(sources):
            raise ValueError('Unknown source.')
        source = sources[int(match[1])-1]
        quote = normalize(claim['quote'])
        if len(quote) < 20 or quote not in normalize(source['text']):
            raise ValueError('Quotation not found in cited passage.')
        checked.append({**claim, 'paper_name': source['paper_name'], 'page_number': source['page_number']})
    return checked

def render_answer(claims):
    if not claims:
        return 'The retrieved passages do not provide enough evidence to answer this question.'
    lines = ['Draft answer — quotations checked against retrieved text; claim support still needs human review.']
    for claim in claims:
        lines.append(f"\n{claim['text']} [{claim['source_id']}]\nExcerpt: {claim['quote']}\nSource: {claim['paper_name']}, page {claim['page_number']}")
    return '\n'.join(lines)
