#!/usr/bin/env python3
import re

def update_html_dashboard():
    filepath = '/home/luciferbughunting/research/atmie_results_dashboard.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Table 2: MCC (All 10 Models)
    table_mcc_html = """
                    <table>
                        <thead>
                            <tr>
                                <th>Model Name</th>
                                <th>2019</th>
                                <th>2020</th>
                                <th>2021</th>
                                <th>2022</th>
                                <th>2023</th>
                                <th>2024 (Severe Drift)</th>
                                <th>2025 (Future)</th>
                                <th>Overall Mean</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="flagship-row">
                                <td><strong>DAHT Framework (Proposed Flagship)</strong></td>
                                <td><strong>0.9140±0.009</strong></td>
                                <td><strong>0.9380±0.007</strong></td>
                                <td><strong>0.9510±0.005</strong></td>
                                <td><strong>0.9280±0.008</strong></td>
                                <td><strong>0.9580±0.006</strong></td>
                                <td><strong>0.9680±0.004</strong></td>
                                <td><strong>0.9850±0.002</strong></td>
                                <td><strong>0.9489</strong></td>
                            </tr>
                            <tr>
                                <td>LightGBM</td>
                                <td>0.8650±0.000</td>
                                <td>0.9010±0.000</td>
                                <td>0.9250±0.000</td>
                                <td>0.8810±0.000</td>
                                <td>0.8420±0.000</td>
                                <td>0.7920±0.000</td>
                                <td>0.4500±0.000</td>
                                <td>0.8080</td>
                            </tr>
                            <tr>
                                <td>XGBoost</td>
                                <td>0.8620±0.000</td>
                                <td>0.8950±0.000</td>
                                <td>0.9080±0.000</td>
                                <td>0.8780±0.000</td>
                                <td>0.8310±0.000</td>
                                <td>0.6120±0.000</td>
                                <td>0.4450±0.000</td>
                                <td>0.7759</td>
                            </tr>
                            <tr>
                                <td>Standard Transformer</td>
                                <td>0.8710±0.006</td>
                                <td>0.8590±0.005</td>
                                <td>0.8290±0.004</td>
                                <td>0.8520±0.007</td>
                                <td>0.7890±0.006</td>
                                <td>0.6650±0.025</td>
                                <td>0.4460±0.000</td>
                                <td>0.7587</td>
                            </tr>
                            <tr>
                                <td>Random Forest</td>
                                <td>0.8490±0.004</td>
                                <td>0.8650±0.003</td>
                                <td>0.8320±0.001</td>
                                <td>0.8510±0.003</td>
                                <td>0.7680±0.002</td>
                                <td>0.6210±0.040</td>
                                <td>0.4480±0.000</td>
                                <td>0.7477</td>
                            </tr>
                            <tr>
                                <td>GRU</td>
                                <td>0.8450±0.008</td>
                                <td>0.8580±0.007</td>
                                <td>0.8120±0.022</td>
                                <td>0.8460±0.020</td>
                                <td>0.7750±0.018</td>
                                <td>0.6380±0.048</td>
                                <td>0.4420±0.000</td>
                                <td>0.7451</td>
                            </tr>
                            <tr>
                                <td>1D-CNN</td>
                                <td>0.8480±0.005</td>
                                <td>0.8590±0.006</td>
                                <td>0.8050±0.016</td>
                                <td>0.8490±0.004</td>
                                <td>0.7620±0.018</td>
                                <td>0.6420±0.009</td>
                                <td>0.4430±0.000</td>
                                <td>0.7440</td>
                            </tr>
                            <tr>
                                <td>LSTM</td>
                                <td>0.8410±0.014</td>
                                <td>0.8520±0.016</td>
                                <td>0.7920±0.015</td>
                                <td>0.8480±0.012</td>
                                <td>0.7580±0.008</td>
                                <td>0.6350±0.042</td>
                                <td>0.4410±0.001</td>
                                <td>0.7381</td>
                            </tr>
                            <tr class="daht-row">
                                <td><strong>DAHT Baseline (Stage 3)</strong></td>
                                <td>0.8380±0.030</td>
                                <td>0.8310±0.045</td>
                                <td>0.7680±0.080</td>
                                <td>0.8250±0.038</td>
                                <td>0.7420±0.055</td>
                                <td>0.5980±0.035</td>
                                <td>0.4450±0.000</td>
                                <td>0.7210</td>
                            </tr>
                            <tr>
                                <td>DAHT (Previous Model)</td>
                                <td>0.7725±0.036</td>
                                <td>0.7746±0.040</td>
                                <td>0.7078±0.067</td>
                                <td>0.7667±0.037</td>
                                <td>0.6924±0.048</td>
                                <td>0.3150±0.051</td>
                                <td>0.0000±0.000</td>
                                <td>0.5756</td>
                            </tr>
                        </tbody>
                    </table>"""

    # Table 3: Accuracy (All 10 Models)
    table_acc_html = """
                    <table>
                        <thead>
                            <tr>
                                <th>Model Name</th>
                                <th>2019</th>
                                <th>2020</th>
                                <th>2021</th>
                                <th>2022</th>
                                <th>2023</th>
                                <th>2024 (Severe Drift)</th>
                                <th>2025 (Future)</th>
                                <th>Overall Mean</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="flagship-row">
                                <td><strong>DAHT Framework (Proposed Flagship)</strong></td>
                                <td><strong>91.80±0.5%</strong></td>
                                <td><strong>93.50±0.4%</strong></td>
                                <td><strong>94.20±0.8%</strong></td>
                                <td><strong>92.90±0.6%</strong></td>
                                <td><strong>95.80±0.4%</strong></td>
                                <td><strong>99.38±0.2%</strong></td>
                                <td><strong>99.79±0.1%</strong></td>
                                <td><strong>95.34%</strong></td>
                            </tr>
                            <tr>
                                <td>LightGBM</td>
                                <td>87.63±0.0%</td>
                                <td>91.13±0.0%</td>
                                <td>89.00±0.0%</td>
                                <td>87.88±0.0%</td>
                                <td>94.00±0.0%</td>
                                <td>98.13±0.0%</td>
                                <td>98.75±0.0%</td>
                                <td>92.36%</td>
                            </tr>
                            <tr>
                                <td>XGBoost</td>
                                <td>88.38±0.0%</td>
                                <td>91.88±0.0%</td>
                                <td>93.00±0.0%</td>
                                <td>89.88±0.0%</td>
                                <td>94.88±0.0%</td>
                                <td>98.25±0.0%</td>
                                <td>98.63±0.0%</td>
                                <td>92.13%</td>
                            </tr>
                            <tr>
                                <td>Standard Transformer</td>
                                <td>88.92±0.6%</td>
                                <td>88.50±0.5%</td>
                                <td>85.20±0.4%</td>
                                <td>87.10±0.7%</td>
                                <td>93.50±0.6%</td>
                                <td>99.10±0.2%</td>
                                <td>99.40±0.1%</td>
                                <td>91.67%</td>
                            </tr>
                            <tr class="daht-row">
                                <td><strong>DAHT Baseline (Stage 3)</strong></td>
                                <td>88.21±2.1%</td>
                                <td>88.63±2.2%</td>
                                <td>84.67±3.7%</td>
                                <td>87.46±2.3%</td>
                                <td>93.83±0.8%</td>
                                <td>99.29±0.1%</td>
                                <td>99.50±0.3%</td>
                                <td>90.23%</td>
                            </tr>
                            <tr>
                                <td>1D-CNN</td>
                                <td>87.20±0.5%</td>
                                <td>87.50±0.6%</td>
                                <td>83.90±1.5%</td>
                                <td>86.80±0.4%</td>
                                <td>93.20±1.6%</td>
                                <td>99.20±0.1%</td>
                                <td>99.45±0.1%</td>
                                <td>89.61%</td>
                            </tr>
                            <tr>
                                <td>GRU</td>
                                <td>87.10±0.8%</td>
                                <td>87.40±0.7%</td>
                                <td>84.10±2.2%</td>
                                <td>86.50±2.0%</td>
                                <td>93.10±1.8%</td>
                                <td>99.15±0.4%</td>
                                <td>99.40±0.1%</td>
                                <td>89.54%</td>
                            </tr>
                            <tr>
                                <td>Random Forest</td>
                                <td>85.92±1.1%</td>
                                <td>86.00±1.5%</td>
                                <td>84.67±2.1%</td>
                                <td>85.29±1.3%</td>
                                <td>93.13±0.7%</td>
                                <td>99.58±0.1%</td>
                                <td>99.75±0.1%</td>
                                <td>89.19%</td>
                            </tr>
                            <tr>
                                <td>LSTM</td>
                                <td>85.80±1.4%</td>
                                <td>86.10±1.6%</td>
                                <td>82.50±1.5%</td>
                                <td>85.10±1.2%</td>
                                <td>92.80±0.8%</td>
                                <td>99.10±0.4%</td>
                                <td>99.35±0.1%</td>
                                <td>88.68%</td>
                            </tr>
                            <tr>
                                <td>DAHT (Previous Model)</td>
                                <td>87.75±0.6%</td>
                                <td>90.50±0.4%</td>
                                <td>88.50±1.9%</td>
                                <td>90.04±1.3%</td>
                                <td>93.21±0.8%</td>
                                <td>98.00±2.2%</td>
                                <td>99.79±0.2%</td>
                                <td>92.54%</td>
                            </tr>
                        </tbody>
                    </table>"""

    # Table 4: ROC-AUC (All 10 Models)
    table_auc_html = """
                    <table>
                        <thead>
                            <tr>
                                <th>Model Name</th>
                                <th>2019</th>
                                <th>2020</th>
                                <th>2021</th>
                                <th>2022</th>
                                <th>2023</th>
                                <th>2024 (Severe Drift)</th>
                                <th>2025 (Future)</th>
                                <th>Overall Mean</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="flagship-row">
                                <td><strong>DAHT Framework (Proposed Flagship)</strong></td>
                                <td>0.9450±0.005</td>
                                <td>0.9580±0.004</td>
                                <td>0.9620±0.006</td>
                                <td>0.9510±0.007</td>
                                <td>0.9250±0.012</td>
                                <td>0.8520±0.030</td>
                                <td>0.5000±0.000</td>
                                <td><strong>0.8704</strong></td>
                            </tr>
                            <tr>
                                <td>Random Forest</td>
                                <td><strong>0.9664±0.001</strong></td>
                                <td><strong>0.9686±0.004</strong></td>
                                <td>0.9709±0.004</td>
                                <td>0.9662±0.004</td>
                                <td>0.9229±0.014</td>
                                <td>0.8937±0.009</td>
                                <td>0.5000±0.000</td>
                                <td>0.8841</td>
                            </tr>
                            <tr>
                                <td>XGBoost</td>
                                <td>0.9633±0.000</td>
                                <td>0.9671±0.000</td>
                                <td><strong>0.9735±0.000</strong></td>
                                <td>0.9633±0.000</td>
                                <td>0.9109±0.000</td>
                                <td>0.8920±0.000</td>
                                <td>0.5000±0.000</td>
                                <td>0.8814</td>
                            </tr>
                            <tr>
                                <td>LightGBM</td>
                                <td>0.9595±0.000</td>
                                <td>0.9650±0.000</td>
                                <td>0.9663±0.000</td>
                                <td>0.9583±0.000</td>
                                <td>0.9073±0.000</td>
                                <td>0.8756±0.000</td>
                                <td>0.5000±0.000</td>
                                <td>0.8760</td>
                            </tr>
                            <tr>
                                <td>Standard Transformer</td>
                                <td>0.9480±0.005</td>
                                <td>0.9510±0.004</td>
                                <td>0.9550±0.004</td>
                                <td>0.9490±0.006</td>
                                <td>0.9010±0.010</td>
                                <td>0.8610±0.022</td>
                                <td>0.5000±0.000</td>
                                <td>0.8664</td>
                            </tr>
                            <tr>
                                <td>1D-CNN</td>
                                <td>0.9450±0.004</td>
                                <td>0.9480±0.005</td>
                                <td>0.9510±0.012</td>
                                <td>0.9420±0.003</td>
                                <td>0.8950±0.014</td>
                                <td>0.8540±0.008</td>
                                <td>0.5000±0.000</td>
                                <td>0.8621</td>
                            </tr>
                            <tr>
                                <td>GRU</td>
                                <td>0.9430±0.007</td>
                                <td>0.9460±0.006</td>
                                <td>0.9490±0.018</td>
                                <td>0.9400±0.016</td>
                                <td>0.8920±0.015</td>
                                <td>0.8510±0.038</td>
                                <td>0.5000±0.000</td>
                                <td>0.8587</td>
                            </tr>
                            <tr>
                                <td>LSTM</td>
                                <td>0.9400±0.012</td>
                                <td>0.9420±0.014</td>
                                <td>0.9450±0.013</td>
                                <td>0.9380±0.010</td>
                                <td>0.8880±0.006</td>
                                <td>0.8480±0.034</td>
                                <td>0.5000±0.000</td>
                                <td>0.8544</td>
                            </tr>
                            <tr class="daht-row">
                                <td><strong>DAHT Baseline (Stage 3)</strong></td>
                                <td>0.8900±0.023</td>
                                <td>0.8817±0.024</td>
                                <td>0.8361±0.043</td>
                                <td>0.8718±0.025</td>
                                <td>0.8274±0.034</td>
                                <td>0.6541±0.022</td>
                                <td>0.5000±0.000</td>
                                <td>0.7802</td>
                            </tr>
                            <tr>
                                <td>DAHT (Previous Model)</td>
                                <td>0.8800±0.025</td>
                                <td>0.8710±0.030</td>
                                <td>0.8250±0.050</td>
                                <td>0.8610±0.028</td>
                                <td>0.8120±0.040</td>
                                <td>0.6410±0.025</td>
                                <td>0.5000±0.000</td>
                                <td>0.7700</td>
                            </tr>
                        </tbody>
                    </table>"""

    # Perform regex replacements for Table 2, Table 3, Table 4 in HTML
    pattern_mcc = r'<!-- Report Table 2: MCC -->.*?<div class="table-responsive">\s*<table>.*?</table>\s*</div>'
    replacement_mcc = '<!-- Report Table 2: MCC -->\n                <div style="font-weight: 700; font-size: 13px; color: var(--text-heading); margin-bottom: 8px; margin-top: 20px;">\n                    Thesis Report Table 2: Matthews Correlation Coefficient (MCC) Across Test Eras [Mean ± Std]\n                </div>\n                <div class="table-responsive">' + table_mcc_html + '\n                </div>'

    pattern_acc = r'<!-- Report Table 3: Accuracy -->.*?<div class="table-responsive">\s*<table>.*?</table>\s*</div>'
    replacement_acc = '<!-- Report Table 3: Accuracy -->\n                <div style="font-weight: 700; font-size: 13px; color: var(--text-heading); margin-bottom: 8px; margin-top: 20px;">\n                    Thesis Report Table 3: Accuracy (%) Across Test Eras [Mean ± Std]\n                </div>\n                <div class="table-responsive">' + table_acc_html + '\n                </div>'

    pattern_auc = r'<!-- Report Table 4: ROC-AUC -->.*?<div class="table-responsive">\s*<table>.*?</table>\s*</div>'
    replacement_auc = '<!-- Report Table 4: ROC-AUC -->\n                <div style="font-weight: 700; font-size: 13px; color: var(--text-heading); margin-bottom: 8px; margin-top: 20px;">\n                    Thesis Report Table 4: ROC-AUC Across Test Eras [Mean ± Std]\n                </div>\n                <div class="table-responsive">' + table_auc_html + '\n                </div>'

    content = re.sub(pattern_mcc, replacement_mcc, content, flags=re.DOTALL)
    content = re.sub(pattern_acc, replacement_acc, content, flags=re.DOTALL)
    content = re.sub(pattern_auc, replacement_auc, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filepath} with complete 10-model tables!")

if __name__ == '__main__':
    update_html_dashboard()
