# 🎓 Academic Forge

<div align="center">

**A curated skill collection for academic writing and research**

[![[99 Assets/Images/0d356e72fcfaae41be0d7adf6fad1c69_MD5.svg]]](https://opensource.org/licenses/MIT)
[![[99 Assets/Images/b998ac00d5de9bdfa6f6e7a1d54ba46b_MD5.svg]]](./skills)

</div>

## 📖 What is a Forge?

The name "Forge" is inspired by **Minecraft's mod loader system** (like Forge or Fabric), which allows players to run multiple mods together seamlessly. Just as Minecraft Forge provides a modpack that integrates various mods for specific gameplay experiences, **Academic Forge** integrates multiple Claude Code skills for a focused academic writing workflow.

### Why "Forge"?

- 🔧 **Integration over Installation** - Just like Minecraft modpacks, you get a curated collection that works well together
- 🎯 **Purpose-Built** - Each forge targets a specific domain (academic writing, web development, data science, etc.)
- 🔄 **Automatic Updates** - Skills remain linked to their original repositories via git submodules
- 🤝 **Community-Driven** - Built on the excellent work of multiple skill creators

## 🎯 Purpose

Academic Forge solves a common problem: **too many skills lead to poor AI agent accuracy**. By curating only the skills relevant to academic writing and research, Claude Code can:

- ✅ Make more precise skill invocations
- ✅ Avoid confusion between similar skills
- ✅ Maintain focus on your research workflow
- ✅ Stay up-to-date with improvements from original authors

## 📦 Included Skills

This forge integrates the following carefully selected skills:

### [claude-scientific-skills](https://github.com/k-dense-ai/claude-scientific-skills) (140 Skills)
- **Author**: [@k-dense-ai](https://github.com/k-dense-ai) - By K-Dense Inc.
- **License**: MIT
- **Coverage**: 140 ready-to-use scientific skills across 15+ domains
- **What It Includes**:
  - 🧬 **Bioinformatics & Genomics** - BioPython, Scanpy, single-cell RNA-seq, variant annotation
  - 🧪 **Cheminformatics & Drug Discovery** - RDKit, DeepChem, molecular docking, virtual screening
  - 🏥 **Clinical Research** - ClinicalTrials.gov, ClinVar, FDA databases, pharmacogenomics
  - 📊 **Data Analysis** - Statistical analysis, matplotlib, seaborn, publication figures
  - 📚 **Scientific Communication** - LaTeX formatting, citation management, peer review
  - 🔬 **Laboratory Automation** - PyLabRobot, Benchling, Opentrons integration
  - 🤖 **Machine Learning** - PyTorch Lightning, scikit-learn, deep learning workflows
  - 📚 **Databases** - 28+ scientific databases (PubMed, OpenAlex, ChEMBL, UniProt, etc.)
- **Best For**: Multi-step scientific workflows from literature review to publication

### [AI-research-SKILLs](https://github.com/zechenzhangAGI/AI-research-SKILLs) (82 Skills)
- **Author**: [@zechenzhangAGI](https://github.com/zechenzhangAGI) - By Orchestra Research
- **License**: MIT
- **Coverage**: 82 expert-level AI research engineering skills across 20 categories
- **What It Includes**:
  - 🏗️ **Model Architecture** - LitGPT, Mamba, RWKV, NanoGPT, TorchTitan (5 skills)
  - 🎯 **Fine-Tuning** - Axolotl, LLaMA-Factory, PEFT, Unsloth (4 skills)
  - 🎓 **Post-Training** - TRL, GRPO, OpenRLHF, SimPO, verl (8 skills for RLHF/DPO)
  - ⚡ **Distributed Training** - DeepSpeed, FSDP, Megatron-Core, Accelerate (6 skills)
  - 🚀 **Optimization** - Flash Attention, bitsandbytes, GPTQ, AWQ (6 skills)
  - 🔥 **Inference** - vLLM, TensorRT-LLM, SGLang, llama.cpp (4 skills)
  - 📊 **Evaluation** - lm-eval-harness, BigCode, NeMo Evaluator (3 skills)
  - 🤖 **Agents & RAG** - LangChain, LlamaIndex, Chroma, FAISS (9 skills)
  - 🎨 **Multimodal** - CLIP, Whisper, LLaVA, Stable Diffusion (7 skills)
  - 📝 **ML Paper Writing** - LaTeX templates for NeurIPS, ICML, ICLR, ACL (1 skill)
- **Documentation Quality**: ~420 lines per skill + 300KB+ reference materials
- **Best For**: AI research workflows from hypothesis to paper publication

### [humanizer](https://github.com/blader/humanizer)
- **Author**: [@blader](https://github.com/blader)
- **License**: Check original repository
- **Purpose**: Refining academic tone, improving readability, avoiding AI-detection patterns
- **Best For**: Polishing drafts, maintaining academic voice, peer review preparation

> **Note**: All skills retain their original licenses and authorship. This forge provides convenient integration only. See [ATTRIBUTIONS.md](./ATTRIBUTIONS.md) for detailed credits.

## 🚀 Quick Start

### Installation

Install Academic Forge directly into your Claude Code project:

```bash
# Navigate to your project
cd your-project

# Install the forge
curl -sSL https://raw.githubusercontent.com/HughYau/AcademicForge/main/scripts/install.sh | bash
```

Or manually:

```bash
# Clone with all submodules
git clone --recursive https://github.com/HughYau/AcademicForge .opencode/skills/academic-forge

# Or if you already cloned without --recursive
git submodule update --init --recursive
```

### Download Skills Submodules

If you only want to download the skills submodules (without the entire repository):

**Windows (PowerShell):**
```powershell
.\scripts\download-skills.ps1
```

**Linux/macOS:**
```bash
bash scripts/download-skills.sh
```

These scripts will automatically download all skills submodules to your local `skills/` folder. For detailed usage instructions, see [scripts/SKILLS-DOWNLOAD-README.md](./scripts/SKILLS-DOWNLOAD-README.md).

### Update Skills

Keep all skills up-to-date with the latest improvements:

```bash
cd .opencode/skills/academic-forge
./scripts/update.sh
```

#### 🔄 Automatic Updates

This repository is configured with automated workflows that update all submodules to their latest versions **every Monday at 09:00 UTC**. This means:

- ✅ Skills always stay up-to-date
- ✅ Automatically receive improvements and bug fixes from original authors
- ✅ No need to manually run update scripts
- 📅 Update schedule: Every Monday at 09:00 UTC

## 🏗️ Structure

```
academic-forge/
├── README.md              # This file
├── LICENSE                # MIT License for the forge structure
├── ATTRIBUTIONS.md        # Detailed credits for all included skills
├── forge.yaml             # Forge metadata and skill configuration
├── .gitmodules            # Git submodule definitions
├── skills/
│   ├── claude-scientific-skills/    (submodule)
│   ├── AI-research-SKILLs/          (submodule)
│   └── humanizer/                   (submodule)
└── scripts/
    ├── install.sh         # Installation script
    └── update.sh          # Update all skills to latest versions
```

## 🎓 Use Cases

Academic Forge is perfect for:

- 📝 **Writing Research Papers** - From outline to submission-ready manuscript
- 🔬 **Experimental Design** - Planning and documenting research methodology
- 📊 **Data Analysis** - Statistical analysis and result interpretation
- 📚 **Literature Review** - Organizing and synthesizing academic sources
- ✍️ **Thesis Writing** - Long-form academic document management
- 👥 **Collaborative Research** - Maintaining consistent style across team members

## 🔄 Version Management

Academic Forge uses git submodules to track specific versions of each skill:

- **Automatic Updates**: Run `./scripts/update.sh` to pull latest changes
- **Version Locking**: Commit the `.gitmodules` state to lock specific versions
- **Rollback Safety**: Use git to revert to previous working states

## 🤝 Contributing

Found a skill that would be perfect for academic writing? Here's how to contribute:

1. **Suggest a Skill** - Open an issue with the skill repository and use case
2. **Test Compatibility** - Ensure it doesn't conflict with existing skills
3. **Submit PR** - Add as a submodule with proper attribution
4. **Update Docs** - Add to README.md and ATTRIBUTIONS.md

### Creating Your Own Forge

Inspired to create a forge for your domain? Great! Here's the template:

```bash
# Fork this repository
# Replace skills with your domain-specific collection
# Update README.md with your forge's purpose
# Share with the community!
```

## 📄 License

The **forge structure** (scripts, configuration, documentation) is licensed under the [MIT License](./LICENSE).

**Individual skills** retain their original licenses - see [ATTRIBUTIONS.md](./ATTRIBUTIONS.md) and each skill's repository for details.


## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/HughYau/AcademicForge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/HughYau/AcademicForge/discussions)
- **Updates**: Watch this repository for new skill additions

---

<div align="center">

**Built with 💙 for the academic research community**

⭐ If this forge helps your research, please star this repo and the individual skill repositories!

</div>
