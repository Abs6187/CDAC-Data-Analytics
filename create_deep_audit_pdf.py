"""Generate the C-DAC Data Analytics syllabus-to-repository audit."""

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import CondPageBreak, Paragraph, SimpleDocTemplate, Table, TableStyle

TITLE = "CDAC PGCP-AI Data Analytics"
PDF_NAME = "CDAC_PGCP_AI_Data_Analytics_Repository_Audit.pdf"
SYLLABUS = "Lakshit_notes/03_Data Analytics.pdf"
FOUND = "notes/01_foundations_and_eda.md"
STATS = "notes/02_statistics_and_probability.md"
MODELS = "notes/03_predictive_and_prescriptive_analytics.md"
EVAL = "notes/04_evaluation_advanced_analytics_powerbi.md"
TESTS = "Day3/O02_statistics_and_hypothesis_testing.py"

# Each entry records a syllabus group, its printed page, and audited topic clusters.
# Evidence levels distinguish standalone labs, embedded code, theory, and gaps.
AUDIT = [
    ("1-2", "1", [
        ("Business analytics, case studies and project lifecycle", "Notes", FOUND,
         "Case examples and six lifecycle phases, including deployment and operations."),
        ("Notebook setup and library orientation", "Notes", FOUND,
         "Jupyter/Colab setup guidance and library imports."),
        ("NumPy and Pandas practice", "Lab", "Day2/O2Pandas/O02_data_frame.py; Day2/O1Numpy/O03_vectorized_math.py",
         "DataFrame operations and NumPy vectorization exercises."),
        ("Lifecycle governance", "Gap", FOUND,
         "No end-to-end project artifact with QA sign-off, management approval and acceptance was verified."),
    ]),
    ("3", "1", [
        ("Nature of data, analytics tools and reporting", "Notes", FOUND,
         "Explains data types, tool choices and the distinction between analysis and reporting."),
        ("Explore and analyze a dataset", "Lab", "Day11/EDA/02_univariate_and_multivariate_audits.ipynb",
         "Univariate and multivariate exploratory checks."),
    ]),
    ("4", "2", [
        ("Exploration and visualization with Matplotlib and Seaborn", "Lab", "Day11/EDA/04_eda_story_extraction.ipynb",
         "Explores a dataset with plots and draws an analytical narrative."),
        ("Business decisions from data", "Notes", FOUND,
         "Case examples and guidance for interpreting visual patterns."),
    ]),
    ("5", "2", [
        ("Mean, median and mode", "Lab", "Day7/01_statistical_measure/01_measures_of_central_tendency_updated.ipynb",
         "Compares measures of location on example data."),
        ("Range, variance, standard deviation and coefficient of variation", "Lab",
         "Day7/01_statistical_measure/02_measures_of_dispersion_variability_spread.ipynb",
         "Measures and compares variability."),
        ("Quartiles, percentiles and IQR", "Lab", "Day4/O05_percentile_methods.py",
         "Calculates percentile positions and interquartile range."),
    ]),
    ("6-7", "2", [
        ("Samples, populations and sampling concepts", "Lab", "Day5/O01_data_population.ipynb",
         "Data population and sampling examples."),
        ("Sample spaces, events and probability rules", "Notes", STATS,
         "Joint, marginal and conditional probabilities and Bayes' theorem."),
        ("Fit and predict with Naive Bayes", "Gap", STATS,
         "Bayes' rule is explained. A dataset-based Naive Bayes classifier lab was not verified."),
        ("Structured resampling comparison", "Gap", STATS,
         "No dedicated lab comparing univariate, paired and resampling designs was verified."),
    ]),
    ("8", "2", [
        ("Random variables and normal, binomial and Poisson distributions", "Lab", TESTS,
         "Computes probabilities and plots continuous and discrete distributions."),
        ("Normal simulation and SciPy distribution checks", "Lab", "Day6/01_Continuous_Probability_Distributions.ipynb",
         "Continuous distribution simulation includes a Kolmogorov-Smirnov check."),
        ("Central Limit Theorem", "Lab", TESTS,
         "Illustrates the sampling distribution of the mean."),
    ]),
    ("9", "2", [
        ("Sampling designs", "Lab", "Day5/O01_data_population.ipynb",
         "Contains sampling examples, including stratified sampling."),
        ("Estimation and statistical interfaces", "Lab", "Day6/05_assignment4_delivery_time_estimator.py",
         "Delivery-time estimation example complements the sampling material."),
    ]),
    ("10", "2-3", [
        ("Covariance and Pearson correlation", "Lab", "Day8/03_bivariate_relationships/01_covariance_and_pearson_correlation.ipynb",
         "Calculates and visualizes bivariate association."),
        ("Outlier detection and treatment", "Walkthrough", STATS,
         "IQR and Z-score detection with trimming and winsorization."),
    ]),
    ("11-12", "3", [
        ("Hypothesis testing and chi-square", "Lab", TESTS,
         "Demonstrates test decisions and chi-square independence on a contingency table."),
        ("One-sample Z-test", "Walkthrough", STATS,
         "Computes the statistic and a two-tailed p-value."),
        ("Skewness", "Lab", "Day4/O06_skewness.py",
         "Demonstrates distribution asymmetry."),
    ]),
    ("13", "3", [
        ("Predictive modeling overview, applications, types and tools", "Notes", MODELS,
         "Summarizes use cases, benefits, limitations and modeling tools."),
        ("Future of predictive modeling", "Gap", MODELS,
         "Dedicated coverage of future directions was not verified in the cited module."),
    ]),
    ("14-16", "3", [
        ("Informative attributes, progressive splits and supervised segmentation", "Walkthrough", MODELS,
         "Explains information gain and impurity, then fits a decision tree."),
        ("Rules and probability estimates", "Walkthrough", MODELS,
         "Exports tree rules and predicts class probabilities."),
        ("Visualizing segmentation", "Notes", MODELS,
         "Includes an explanatory diagram and text rules. A plotted fitted tree was not verified."),
        ("Predictive versus prescriptive modeling", "Notes", MODELS,
         "Contrasts predictions with decisions and describes prescriptive use cases."),
    ]),
    ("17-18", "3", [
        ("Regression analysis", "Walkthrough", MODELS,
         "Fits multiple linear regression on synthetic data and discusses coefficients and collinearity."),
        ("Forecasting techniques", "Gap", MODELS,
         "A time-ordered forecast and out-of-sample evaluation were not verified."),
    ]),
    ("19-20", "3", [
        ("Simulation and risk analysis", "Lab", "Day6/05_assignment4_delivery_time_estimator.py; Day6/06_assignment5_qc_bottling_audit.py",
         "Operational simulation and quality-control examples. The modeling notes discuss Monte Carlo risk."),
        ("Linear optimization", "Walkthrough", MODELS,
         "Solves a bounded production planning problem with scipy.optimize.linprog."),
        ("Nonlinear optimization", "Gap", MODELS,
         "A nonlinear objective or constraint example was not verified."),
    ]),
    ("21", "3", [
        ("Overfitting, generalization and holdout evaluation", "Notes", EVAL,
         "Explains generalization and contrasts a holdout split with cross-validation."),
        ("Stratified cross-validation", "Walkthrough", EVAL,
         "Uses StratifiedKFold and cross_val_score with F1."),
    ]),
    ("22", "4", [
        ("Classifier evaluation", "Walkthrough", EVAL,
         "Computes a confusion matrix, classification metrics and ROC-AUC."),
        ("Decision framework and investment implications", "Notes", EVAL,
         "Explains misclassification costs and expected value for data investments."),
        ("Explicit baseline comparison", "Gap", EVAL,
         "A scored baseline classifier alongside the trained model was not verified."),
    ]),
    ("23", "4", [
        ("Combining evidence with Bayes' rule", "Notes", EVAL,
         "Explains sequential evidence updates and probabilistic reasoning."),
    ]),
    ("24", "4", [
        ("Factor analysis", "Notes", EVAL,
         "Explains the latent-factor model and contrasts it with PCA. The code lab fits PCA."),
        ("Directional and functional data analysis", "Notes", EVAL,
         "Defines circular data and curve-valued observations with examples."),
        ("Advanced methods implementation", "Gap", EVAL,
         "A fitted factor model, circular-statistics exercise and functional data analysis workflow were not verified."),
    ]),
    ("25", "4", [
        ("Power BI architecture, interface and data modeling", "Notes", EVAL,
         "Explains the Power BI ecosystem, star schema, and measures versus calculated columns."),
        ("Power Query, reports and dashboards", "Notes", EVAL,
         "Describes the Power Query transformation and reporting pipeline."),
        ("Hands-on Power BI workflow", "Gap", EVAL,
         "No Power BI project or report demonstrating transformations, interactive charts and sharing was verified."),
    ]),
]

NAVY = colors.HexColor("#1A365D")
SLATE = colors.HexColor("#4A5568")
RULE = colors.HexColor("#CBD5E0")
EVIDENCE_COLORS = {
    "Lab": "#176044",
    "Walkthrough": "#24598C",
    "Notes": "#655218",
    "Gap": "#8B2634",
}


class AuditCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_states = []

    def showPage(self):
        self.page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        for state in self.page_states:
            self.__dict__.update(state)
            self.draw_page_furniture(len(self.page_states))
            super().showPage()
        super().save()

    def draw_page_furniture(self, total):
        width, height = A4
        self.saveState()
        self.setStrokeColor(RULE)
        self.setLineWidth(0.6)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(NAVY)
            self.drawString(32, height - 20, f"{TITLE} | Repository Audit")
            self.setFont("Helvetica", 7.5)
            self.setFillColor(SLATE)
            self.drawString(32, height - 32, "ACTS Pune teaching guidelines | DATA_ANALYTICS_CDAC")
            self.line(32, height - 39, width - 32, height - 39)
        self.line(32, 32, width - 32, 32)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(SLATE)
        self.drawString(32, 21, "Official benchmark: ACTS Pune PGCP-AI | 120 hours (50T + 50L + 20SL)")
        self.drawRightString(width - 32, 21, f"Page {self._pageNumber} of {total}")
        self.restoreState()


def build_pdf(filename):
    doc = SimpleDocTemplate(str(filename), pagesize=A4, title=f"{TITLE} - Repository Audit",
                            leftMargin=32, rightMargin=32, topMargin=47, bottomMargin=43)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle("AuditTitle", parent=styles["Title"], fontSize=18, leading=22,
                              alignment=0, textColor=NAVY, spaceAfter=3))
    styles.add(ParagraphStyle("AuditHeading", parent=styles["Heading2"], fontSize=12, leading=15,
                              textColor=NAVY, spaceBefore=12, spaceAfter=5, keepWithNext=False))
    styles.add(ParagraphStyle("AuditBody", parent=styles["Normal"], fontSize=9, leading=13,
                              textColor=SLATE, spaceAfter=7))
    styles.add(ParagraphStyle("AuditCell", parent=styles["Normal"], fontSize=8, leading=10.6,
                              textColor=colors.HexColor("#1A202C")))
    styles.add(ParagraphStyle("AuditHeader", parent=styles["AuditCell"], fontName="Helvetica-Bold",
                              textColor=colors.white))

    def table(headers, rows, widths, color):
        heading = [Paragraph(escape(text), styles["AuditHeader"]) for text in headers]
        cells = [[Paragraph(text, styles["AuditCell"]) for text in row] for row in rows]
        grid = Table([heading, *cells], colWidths=widths, repeatRows=1, hAlign="LEFT")
        grid.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), color),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F3F6FA")]),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("INNERGRID", (0, 0), (-1, -1), 0.35, RULE),
            ("BOX", (0, 0), (-1, -1), 0.6, RULE),
        ]))
        return grid

    rows, covered, gaps = [], [], []
    for sessions, page, topics in AUDIT:
        reference = f"<b>{sessions}</b><br/>p. {page}"
        counts = {level: sum(topic[1] == level for topic in topics) for level in EVIDENCE_COLORS}
        coverage = "<br/>".join(f"{level}: {count}" for level, count in counts.items() if count)
        rows.append((reference, escape("; ".join(topic[0] for topic in topics)), coverage))
        for topic, level, paths, detail in topics:
            evidence = "<br/>".join(f"<font name='Courier' size='7'>{escape(path)}</font>"
                                   for path in paths.split("; "))
            label = f"<font color='{EVIDENCE_COLORS[level]}'><b>{level}</b></font>"
            row = (reference, f"<b>{escape(topic)}</b><br/>{label}",
                   f"{evidence}<br/>{escape(detail)}")
            (gaps if level == "Gap" else covered).append(row)

    story = [
        Paragraph(TITLE, styles["AuditTitle"]),
        Paragraph("<b>Repository Audit | Curriculum Coverage and Practical Gaps</b>", styles["AuditBody"]),
        Paragraph(f"<b>Benchmark</b> ACTS Pune, PGCP-AI August 2026, Sessions 1-25. "
                  f"<br/><b>Official syllabus</b> {escape(SYLLABUS)} "
                  "<br/><b>Audit scope</b> Local DATA_ANALYTICS_CDAC checkout, including course notes and lab source.",
                  styles["AuditBody"]),
        Paragraph(f"<b>{len(covered)} topic clusters with evidence | {len(gaps)} gaps</b><br/>"
                  "<b>Lab</b> = standalone script or notebook. <b>Walkthrough</b> = code embedded in notes. "
                  "<b>Notes</b> = documented explanation. <b>Gap</b> = syllabus topic or practice without "
                  "verified evidence in the reviewed checkout. Evidence was inspected as source.",
                  styles["AuditBody"]),
        CondPageBreak(85),
        Paragraph("1. Session-by-session coverage", styles["AuditHeading"]),
        table(("Sessions / PDF page", "Official topic clusters", "Evidence tally"), rows, [75, 353, 91], NAVY),
        CondPageBreak(85),
        Paragraph("2. Practical and curriculum gaps", styles["AuditHeading"]),
        table(("Sessions / PDF page", "Topic / evidence", "Closest reference and gap"), gaps,
              [75, 151, 293], colors.HexColor("#842029")),
        CondPageBreak(85),
        Paragraph("3. Topics with repository evidence", styles["AuditHeading"]),
        table(("Sessions / PDF page", "Topic / evidence", "Repository file and what it contains"), covered,
              [75, 151, 293], colors.HexColor("#176044")),
    ]
    doc.build(story, canvasmaker=AuditCanvas)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path, default=Path(__file__).with_name(PDF_NAME))
    args = parser.parse_args()
    build_pdf(args.output)
    print(f"Generated {args.output}")
