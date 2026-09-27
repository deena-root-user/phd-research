#!/usr/bin/env python3
import re
import os

def update_html():
    filepath = '/home/luciferbughunting/research/atmie_results_dashboard.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Exact Replacements for HTML
    content = content.replace('ATMIE & DAHT Master PhD Dissertation Research Dashboard', 'DAHT Master PhD Dissertation Research Dashboard')
    content = content.replace('ATMIE & DAHT Master PhD Results Dashboard', 'DAHT Master PhD Results Dashboard')
    content = content.replace('Adaptive Temporal Malware Intelligence Engine & DAHT Benchmark', 'Domain-Aware Hierarchical Transformer (DAHT) Research Benchmark')
    content = content.replace('ATMIE-Upgrade (Proposed Flagship: 95.34% Acc / 0.9639 F1)', 'DAHT Framework (Proposed Flagship: 95.34% Acc / 0.9639 F1)')
    content = content.replace('DAHT Framework (Stage 3: 90.23% Acc / 0.7785 F1)', 'DAHT Baseline (Stage 3: 90.23% Acc / 0.7785 F1)')
    content = content.replace('ATMIE-Upgrade Out-of-Time Acc', 'DAHT Framework Out-of-Time Acc')
    content = content.replace('ATMIE-Upgrade Macro F1', 'DAHT Framework Macro F1')
    content = content.replace('DAHT Framework Out-of-Time Acc', 'DAHT Baseline Out-of-Time Acc')
    content = content.replace('DAHT Framework Macro F1', 'DAHT Baseline Macro F1')
    content = content.replace('flagship ATMIE-Upgrade framework', 'flagship DAHT framework')
    content = content.replace('ATMIE-Upgrade Zero-Day Resilience Victory:', 'DAHT Framework Zero-Day Resilience Victory:')
    content = content.replace('ATMIE-Upgrade is the <em>only framework</em>', 'DAHT Framework is the <em>only framework</em>')
    content = content.replace("ATMIE-Upgrade's Dynamic Threshold Calibration", "DAHT's Dynamic Threshold Calibration")
    content = content.replace('Section 2: Mathematical Formulation of ATMIE-Upgrade', 'Section 2: Mathematical Formulation of DAHT Framework')
    content = content.replace('Table 1: Complete Performance Breakdown for ATMIE-Upgrade Across Test Eras', 'Table 1: Complete Performance Breakdown for DAHT Framework Across Test Eras')
    content = content.replace('ATMIE-Upgrade (Proposed Flagship)', 'DAHT Framework (Proposed Flagship)')
    content = content.replace('DAHT (Stage 3 Framework)', 'DAHT Baseline (Stage 3)')
    content = content.replace('DAHT Framework</h4>', 'DAHT Baseline Framework</h4>')
    content = content.replace('Full ATMIE-Upgrade', 'Full DAHT Framework')
    content = content.replace('ATMIE-Upgrade vs LightGBM', 'DAHT Framework vs LightGBM')
    content = content.replace('ATMIE-Upgrade vs XGBoost', 'DAHT Framework vs XGBoost')
    content = content.replace('ATMIE-Upgrade vs Random Forest', 'DAHT Framework vs Random Forest')
    content = content.replace('ATMIE-Upgrade vs Standard Transformer', 'DAHT Framework vs Standard Transformer')
    content = content.replace('ATMIE-Upgrade vs DAHT (Stage 3)', 'DAHT Framework vs DAHT Baseline')
    content = content.replace('ATMIE-Upgrade vs DAHT', 'DAHT Framework vs DAHT Baseline')
    content = content.replace('ATMIE Statistically Superior', 'DAHT Statistically Superior')
    content = content.replace('Slide 2 of 8: Mathematical Formulation of ATMIE-Upgrade', 'Slide 2 of 8: Mathematical Formulation of DAHT Framework')
    
    # Catch any remaining occurrences
    content = content.replace('ATMIE-Upgrade', 'DAHT Framework')
    content = content.replace('ATMIE', 'DAHT')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath} - Remaining 'ATMIE' count: {content.count('ATMIE') + content.count('atmie')}")

def update_md():
    filepath = '/home/luciferbughunting/research/phd_thesis_final_report.md'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('Stage 4: ATMIE-Upgrade (Proposed Flagship): The **Adaptive Temporal Malware Intelligence Engine**', 'Stage 4: DAHT Framework (Proposed Flagship): The **Domain-Aware Hierarchical Transformer**')
    content = content.replace('ATMIE-Upgrade', 'DAHT Framework')
    content = content.replace('ATMIE Statistically Superior', 'DAHT Statistically Superior')
    content = content.replace('ATMIE', 'DAHT')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath} - Remaining 'ATMIE' count: {content.count('ATMIE') + content.count('atmie')}")

def update_docx_builder():
    filepath = '/home/luciferbughunting/research/build_phd_docx_report.py'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('Adaptive Temporal Malware Intelligence Engine (ATMIE-Upgrade)', 'Domain-Aware Hierarchical Transformer (DAHT Framework)')
    content = content.replace('ATMIE-Upgrade Zero-Day Resilience Victory: ', 'DAHT Framework Zero-Day Resilience Victory: ')
    content = content.replace('ATMIE-Upgrade is the flagship framework', 'DAHT Framework is the flagship framework')
    content = content.replace('2. Mathematical Formulation of ATMIE-Upgrade', '2. Mathematical Formulation of DAHT Framework')
    content = content.replace('ATMIE-Upgrade integrates four core mathematical modules', 'DAHT Framework integrates four core mathematical modules')
    content = content.replace('ATMIE-Upgrade (Proposed Flagship)', 'DAHT Framework (Proposed Flagship)')
    content = content.replace('ATMIE Baseline', 'DAHT Baseline')
    content = content.replace('Stage 4: ATMIE-Upgrade (Proposed Flagship)', 'Stage 4: DAHT Framework (Proposed Flagship)')
    content = content.replace('Adaptive Temporal Malware Intelligence Engine', 'Domain-Aware Hierarchical Transformer')
    content = content.replace('Full ATMIE-Upgrade', 'Full DAHT Framework')
    content = content.replace('ATMIE-Upgrade vs LightGBM', 'DAHT Framework vs LightGBM')
    content = content.replace('ATMIE-Upgrade vs XGBoost', 'DAHT Framework vs XGBoost')
    content = content.replace('ATMIE-Upgrade vs Random Forest', 'DAHT Framework vs Random Forest')
    content = content.replace('ATMIE-Upgrade vs Transformer', 'DAHT Framework vs Standard Transformer')
    content = content.replace('ATMIE-Upgrade vs DAHT', 'DAHT Framework vs DAHT Baseline')
    content = content.replace('ATMIE-Upgrade', 'DAHT Framework')
    content = content.replace('ATMIE', 'DAHT')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath} - Remaining 'ATMIE' count: {content.count('ATMIE') + content.count('atmie')}")

if __name__ == '__main__':
    update_html()
    update_md()
    update_docx_builder()
