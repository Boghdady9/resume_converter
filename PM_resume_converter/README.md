# 🚀 PM Resume Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Built%20with-Gradio-orange)](https://gradio.app/)
[![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-green)](https://langchain.com/)

Transform your professional resume into a compelling Product Manager resume using AI-powered intelligence and industry best practices.

## 🎯 Overview

PM Resume Converter is an advanced AI tool that automatically transforms traditional resumes into Product Manager-focused documents. Using LangChain, OpenAI GPT-4, and Pinecone vector database, it intelligently restructures content, enhances achievements with quantifiable metrics, and aligns your experience with PM competencies.

## ✨ Key Features

- **🤖 AI-Powered Transformation**: Leverages GPT-4 to intelligently rewrite resume content  
- **📊 Metrics Enhancement**: Automatically adds quantifiable achievements and impact metrics  
- **🎯 PM-Focused Language**: Translates any experience into PM-relevant competencies  
- **💾 Vector Database**: Uses Pinecone for context-aware transformations based on successful PM resumes  
- **✏️ Interactive Editing**: Chat interface for real-time resume modifications  
- **📋 Section Preservation**: Maintains original structure while enhancing content  
- **🔄 Iterative Refinement**: Make specific edits to any section through natural language  

## 🏗️ Architecture
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   PDF Upload    │────▶│  Text Extractor │────▶│   LangChain     │
│   (Gradio UI)   │     │   (PyMuPDF)     │     │     Agent       │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                          │
                        ┌─────────────────┐     ┌─────────▼────────┐
                        │    Pinecone     │◀────│   OpenAI GPT-4   │
                        │  Vector Store   │     │   Embeddings     │
                        └─────────────────┘     └──────────────────┘



