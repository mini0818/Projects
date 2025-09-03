🧬 DNA Nucleotide Counter Web App

A simple and interactive Streamlit-based web app for analyzing DNA sequences.
Upload or paste a DNA sequence, and the app will calculate nucleotide counts, GC content, reverse complement, and generate visualizations.

🚀 Features

📥 Upload or paste DNA sequences (supports FASTA and TXT formats).

🧾 Cleans and validates sequences automatically.

🔢 Nucleotide counting (A, T, G, C).

🧪 GC content calculation.

🧬 Reverse complement sequence generation.

📊 Interactive visualizations:

Table view of nucleotide counts.

Bar chart (Altair).

Pie chart (Plotly).

💾 Export nucleotide counts as a CSV file.

🎨 Dark mode UI with modern styling.

🛠️ Installation

Clone the repository and install dependencies:

git clone https://github.com/yourusername/dna-nucleotide-counter.git
cd dna-nucleotide-counter
pip install -r requirements.txt


requirements.txt should include:

pandas
streamlit
altair
plotly

▶️ Usage

Run the app locally with:

streamlit run app.py


Then open the app in your browser (default: http://localhost:8501).

📸 App Preview


(Image shown at the top of the app)

📋 Example Input
>DNA Query
GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT

📊 Example Output

Nucleotide Counts:

A: 50
T: 45
G: 55
C: 60


GC Content: 51.25%

Reverse Complement: Shown as a text block in the app.

Charts: Interactive bar and pie charts.

📥 Download

Export nucleotide counts as nucleotide_counts.csv.

🤝 Contributing

Pull requests are welcome! Please open an issue for major changes or new feature ideas.

📜 License

MIT License © 2025
