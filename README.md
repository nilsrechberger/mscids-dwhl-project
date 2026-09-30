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

## Project Struckture

```bash
.
├── .env.example                        # Expample .env file
├── .gitignore                          # Git ignore file
├── pyproject.toml                      # Python project TOML
├── README.md                           # Project documentation
├── src                                 
│   ├── config.py                       # Source code congig
│   └──fetching                        # Data fetching modules
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
souce . .venv/bin/activate
```

### 3. Setup the project

```bash
python -m pip install -e .
```

# Contact

- Nils Rechberger: nils.rechberger@stud.hslu.ch
- Joel Rieser:joel.rieser@stud.hslu.ch
- Timo Schildknecht: timo.schildknecht@stud.hslu.ch
