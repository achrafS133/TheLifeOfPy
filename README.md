# 🧬 TheLifeOfPy

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

*An Artificial Life Simulation powered by Neural Networks and Evolutionary Algorithms*

</div>

---

## 🎬 Demo

<div align="center">

https://github.com/user-attachments/assets/demo.mp4

![TheLifeOfPy Demo](demo.mp4)

*Watch organisms evolve in real-time as they learn to find food and survive!*

</div>

> **📌 Note**: If the video doesn't play above, you can [download and watch demo.mp4](demo.mp4) directly.

---

## 🌟 Overview

**TheLifeOfPy** is a mesmerizing artificial life simulation where digital organisms evolve and adapt to survive in their environment. Each organism is controlled by a neural network "brain" that learns to navigate the world, seek food, and reproduce — all through natural selection.

Watch as simple creatures develop increasingly sophisticated behaviors across generations, demonstrating the power of evolutionary algorithms in action!

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **Neural Network Brains** | Each organism has a 2-layer neural network that processes sensory inputs and controls movement |
| 🧬 **Genetic Evolution** | Offspring inherit mutated versions of their parent's neural network, allowing for adaptation |
| 🍀 **Dynamic Ecosystem** | Organisms compete for food resources that continuously respawn in the environment |
| ⚡ **Energy System** | Realistic energy mechanics — moving costs energy, eating restores it |
| 🔄 **Reproduction** | Organisms that gather enough energy can reproduce, passing their genes to the next generation |
| 📊 **Real-time Stats** | Live population count, generation tracker, and food availability display |

---

## 🏗️ Architecture

```
TheLifeOfPy/
├── main.py           # Entry point - game loop and rendering
├── world.py          # World simulation - manages organisms and food
├── organism.py       # Organism class - sensing, movement, reproduction
├── neural_network.py # Neural network brain implementation
├── food.py           # Food entity class
├── requirements.txt  # Project dependencies
└── demo.mp4          # Demo video
```

### Neural Network Architecture

```
┌─────────────────────────────────────────────────────┐
│                    ORGANISM BRAIN                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│   INPUTS (2)          HIDDEN (6)        OUTPUTS (2) │
│                                                     │
│  ┌──────────┐       ┌──────────┐      ┌──────────┐ │
│  │ Distance │──┬──▶ │          │──┬──▶│  Speed   │ │
│  │ to Food  │  │    │   tanh   │  │   │  Factor  │ │
│  └──────────┘  │    │  neurons │  │   └──────────┘ │
│                │    │          │  │                │
│  ┌──────────┐  │    │          │  │   ┌──────────┐ │
│  │  Angle   │──┴──▶ │          │──┴──▶│ Rotation │ │
│  │ to Food  │       │          │      │          │ │
│  └──────────┘       └──────────┘      └──────────┘ │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/achrafS133/TheLifeOfPy.git
   cd TheLifeOfPy
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Simulation

```bash
python main.py
```

---

## 🎮 How It Works

### Organism Behavior

1. **Sensing** — Each organism detects the nearest food source and calculates:
   - Distance to food (normalized 0-1)
   - Angle difference between current heading and food direction

2. **Decision Making** — The neural network processes these inputs and outputs:
   - Speed factor (how fast to move)
   - Rotation amount (turning direction)

3. **Movement** — Organisms move based on their neural network's decisions, consuming energy proportional to their speed

4. **Survival** — Organisms must eat food to replenish energy. Running out of energy means death!

5. **Reproduction** — When an organism's energy exceeds the reproduction threshold, it splits into two organisms with slightly mutated brains

### Evolution in Action

Over generations, organisms that are better at finding food survive longer and produce more offspring. Their neural network weights are passed on with small mutations, gradually improving the population's foraging ability.

---

## ⚙️ Configuration

You can modify these constants in `main.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `WIDTH` | 1000 | Window width in pixels |
| `HEIGHT` | 800 | Window height in pixels |
| `FPS` | 60 | Frames per second |

And in `world.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `num_organisms` | 20 | Initial population size |
| `num_food` | 50 | Food count maintained in world |

---

## 🧪 Technical Details

### Energy Mechanics

```python
energy_loss = 0.05 + (effective_speed * 0.02) + (radius * 0.005)
```

- Base metabolism: 0.05 per frame
- Movement cost: proportional to speed
- Size cost: larger organisms need more energy

### Mutation

When reproducing, offspring neural networks mutate with:
- **Rate**: 20% chance per weight
- **Magnitude**: ±0.3 maximum change

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

---



## 🙏 Acknowledgments

- Inspired by artificial life simulations and evolutionary computing
- Built with [Pygame](https://www.pygame.org/) and [NumPy](https://numpy.org/)

---

<div align="center">

**⭐ Star this repo if you find it interesting! ⭐**

*Watch life evolve, one frame at a time.*

</div>
