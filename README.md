# On Time in Every Municipality?
A Data Lake and Data Warehouse for Analysing Weather- and Time-Related Delays in Swiss Public Transport at Municipality Level.

```text
  ═══ Line 2    ─── Line 3    │ Line 4    ║ Line 7    ● Station    ≈ Lake

                           [4] [7]
                            │   ║
                            ●   ●  Nordring
                            │   ║
                Lindenplatz ●   ●
                            │   ║
[2]═══●══════════●══════════╪═══╬══════════●══════════●═══[2]
[3]───●──────────●──────────┼───╫──────────●──────────●───[3]
   Westhof    Kreuzweg      │   ║ Zentrum Markt     Ostpark
                            │   ║
               Brückenplatz ●   ●
                            │   ╚═══════════╗
                            │               ║   ≈≈≈≈≈≈
                            ●  Parkring     ●  ≈≈≈≈≈≈≈≈≈
                            │               ║ ≈≈≈≈≈≈≈≈≈≈≈≈
                            │      Seeblick ● ≈≈≈≈ SEE ≈≈≈≈
                            ●  Südbahnhof   ║  ≈≈≈≈≈≈≈≈≈≈≈
                            │               ║   ≈≈≈≈≈≈≈≈≈
                           [4]             [7]
```

## Project Structure

```bash
.
├── .env.example                        # Expample .env file
├── .gitignore                          # Git ignore file
├── pytest.ini                          # Pytest config
├── README.md                           # Project documentation
├── requirements.txt                    # Runtime dependencies
├── requirements-dev.txt                # Dev dependencies (pytest, black)
├── src                                 
│   ├── config.py                       # Source code congig
│   └── loaders                         # Data loaders
├── tests                               # Pytest tests
    ├── test_gtfs_rt.py
    ├── test_municipality.py
    ├── test_transport.py
    └── test_weather.py
```

## Setup

### 1. Clone this repository

```bash
git clone https://github.com/nilsrechberger/mscids-dwl-project.git

cd mscids-dwl-project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv

# For Windows
.venv\Scripts\activate 

# For Mac / Linux
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt

# For development (pytest, black)
python -m pip install -r requirements-dev.txt
```

Run everything from the repository root, e.g. `python -m pytest`.

# Contact

- Nils Rechberger: nils.rechberger@stud.hslu.ch
- Joel Rieser:joel.rieser@stud.hslu.ch
- Timo Schildknecht: timo.schildknecht@stud.hslu.ch
