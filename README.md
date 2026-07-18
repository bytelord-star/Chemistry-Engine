![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-v0.1.0-orange)
# 🧪 Chemistry Engine

> A modular, scalable, and extensible chemistry engine written in Python.

Chemistry Engine is an open-source project designed to analyze, classify, name, and process chemical compounds using a clean, modular architecture.

The long-term vision is to build a complete chemistry framework capable of supporting chemical calculations, reaction prediction, molecular analysis, and AI-assisted chemistry applications.

---

## 🚀 Current Features

### Core Engine
- ✅ Chemical formula parser
- ✅ Formula validation
- ✅ Element validation
- ✅ Polyatomic ion detection
- ✅ JSON-based chemical databases
- ✅ Modular project architecture

### Chemical Analysis
- ✅ Molecular mass calculation
- ✅ Bond type prediction
- ✅ Molecular polarity prediction
- ✅ Compound classification
- ✅ Oxidation number engine (basic)

### IUPAC Naming
- ✅ Molecular compound naming
- ✅ Binary salt naming
- ✅ Polyatomic salt naming
- ✅ Metal oxide naming
- ✅ Nonmetal oxide naming
- ✅ Acid naming
- ✅ Base naming
- ✅ Common name support
- ✅ Transition metal Roman numeral naming (Fe(II), Cu(I), ...)

### Databases
- ✅ Elements database
- ✅ Polyatomic ions database
- ✅ Acid database
- ✅ Base database
- ✅ Common names database
- ✅ Compound database

---

# 📂 Project Structure

```
Chemistry-Engine
│
├── DATA/
│   ├── acid.json
│   ├── bases.json
│   ├── common_names.json
│   ├── compounds.json
│   ├── elements.json
│   ├── periodic_groups.json
│   ├── polyatomic_ions.json
│   ├── reactions.json
│   └── valence_data.json
│
├── models/
│   ├── compound/
│   ├── core/
│   ├── naming/
│   ├── parser/
│   ├── reaction/
│   └── validation/
│
├── tools/
│
├── config.py
├── main.py
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/bytelord-star/Chemistry-Engine.git
```

Move into the project

```bash
cd Chemistry-Engine
```

Run

```bash
python main.py
```

---

# 💡 Example

### Input

```
Fe2O3
```

### Output

```
Formula:
Fe2O3

Name:
Rust

IUPAC Name:
Iron(III) Oxide

Bond Type:
Ionic

Classification:
Metal Oxide
```

---

# 🏗 Architecture

```
                User Input
                     │
                     ▼
            Formula Parser
                     │
                     ▼
          Compound Engine
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
 Classification   Naming Engine  Analysis Engine
        │            │            │
        └────────────┼────────────┘
                     ▼
             Database Managers
                     │
                     ▼
              JSON Databases
```

This modular design allows every subsystem to evolve independently while keeping the project maintainable and scalable.

---

# 🗺 Development Roadmap

## ✅ Version 0.1 (Current)

- Formula parsing
- Formula validation
- Compound classification
- Molecular mass calculation
- Bond prediction
- Molecular polarity prediction
- Acid naming
- Base naming
- Molecular naming
- Salt naming
- Metal oxide naming
- Nonmetal oxide naming
- Oxidation number engine
- Common names
- JSON databases

---

## 🔜 Version 0.2

- Organic compound database
- Solubility database
- Advanced oxidation state engine
- Full transition-metal naming
- Database optimization

---

## 🔬 Version 0.3

- Chemical reaction prediction
- Equation balancing
- Solubility prediction
- Precipitation prediction
- Thermodynamic calculations

---

## 🧬 Version 0.4

- Organic chemistry engine
- Functional group recognition
- Organic nomenclature
- Isomer detection

---

## 🚀 Version 1.0

- AI Chemistry Assistant
- Advanced reaction engine
- Molecular property prediction
- Plugin system
- Public Python API
- Complete chemistry framework

---

# 🎯 Long-Term Vision

The goal of Chemistry Engine is to become a complete open-source chemistry framework for Python that can be used in

- Chemistry education
- Scientific research
- AI chemistry projects
- Molecular analysis
- Chemical simulations
- Automation tools
- Educational software

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Bug reports, feature requests, ideas, and improvements are always appreciated.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Mohamad**

GitHub

https://github.com/bytelord-star

---

⭐ **If you find this project useful, consider giving it a Star on GitHub.**
