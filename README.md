# ABB Sales Presentation Builder

🎯 A Streamlit web application for creating compelling, customer-centric sales presentations for ABB.

## 🚀 Quick Deploy to Streamlit Cloud (FREE)

### Prerequisites
- GitHub account (free)
- Streamlit Cloud account (free - sign up at [share.streamlit.io](https://share.streamlit.io))

### Step-by-Step Deployment Guide

#### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon (top right) → **"New repository"**
3. Repository settings:
   - Name: `abb-sales-presentation-builder`
   - Description: "ABB Sales Presentation Builder"
   - Visibility: **Private** (recommended) or Public
   - ✅ Check "Add a README file"
4. Click **"Create repository"**

#### Step 2: Upload Files to GitHub
1. In your new repository, click **"Add file"** → **"Upload files"**
2. Drag and drop these files:
   - `interface.py`
   - `requirements.txt`
   - `config.toml`
3. Scroll down and click **"Commit changes"**

#### Step 3: Create Folder Structure
1. Click **"Add file"** → **"Create new file"**
2. Type: `.streamlit/config.toml`
3. Copy the content from your `config.toml` file
4. Click **"Commit changes"**

Your repository structure should look like:
```
abb-sales-presentation-builder/
├── interface.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── README.md
```

#### Step 4: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign in with GitHub"** and authorize Streamlit
3. Click **"New app"**
4. Fill in the deployment form:
   - **Repository:** `your-username/abb-sales-presentation-builder`
   - **Branch:** `main` (or `master`)
   - **Main file path:** `interface.py`
   - **App URL:** Choose a custom name (e.g., `abb-sales-builder`)
5. Click **"Deploy!"**

#### Step 5: Wait for Deployment
- First deployment takes 2-3 minutes
- You'll see a "Your app is in the oven" message
- Once ready, you'll get a URL like: `https://abb-sales-builder.streamlit.app`

### 🎉 Done! Your App is Live!

Share the URL with your sales team. Anyone with the link can access it!

---

## 🖥️ Local Development (Optional)

If you want to run it locally on your computer:

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/abb-sales-presentation-builder.git
cd abb-sales-presentation-builder

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run interface.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 📖 How to Use the App

1. **Fill in Required Fields** (marked with *)
   - Customer Name
   - Presentation Language
   - Industry Segment
   - Meeting Context

2. **Add Optional Details** (highly recommended)
   - Customer channel, country, project title
   - Specific application
   - Buyer personas
   - Customer pain points and objectives
   - Technical specifications
   - Competitive information

3. **Generate Input File**
   - Click "Generate Presentation Input File"
   - Review the summary
   - Download the JSON file

4. **Create Your Presentation**
   - Share the JSON file with the ABB AI Assistant
   - The AI will generate a customized PowerPoint presentation
   - Review and refine as needed

---

## 🎨 Features

- ✅ ABB-branded interface with official colors
- ✅ User-friendly form with helpful tooltips
- ✅ Input validation for required fields
- ✅ JSON export for AI processing
- ✅ Mobile-responsive design
- ✅ Progress tracking and confirmation

---

## 🔧 Customization

### Changing ABB Colors
Edit the CSS in `interface.py`:
```python
primaryColor = "#FF000F"  # ABB Red
secondaryColor = "#6764f6"  # ABB Lilac
```

### Adding New Fields
Add new input fields in the form section of `interface.py` and update the `form_data` dictionary.

---

## 📞 Support

**Contact:** Eva de Quintana  
**Email:** eva.de-quintana@es.abb.com  
**Organization:** ABB Spain

---

## 📝 License

© 2026 ABB. All rights reserved.

---

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud](https://share.streamlit.io)
- [ABB.com](https://www.abb.com)
- [ABB Library](https://library.abb.com)

---

## 🐛 Troubleshooting

**App won't deploy?**
- Check that all files are in the correct locations
- Verify `requirements.txt` is present
- Check Streamlit Cloud logs for errors

**Form not working?**
- Clear browser cache
- Try a different browser
- Check console for JavaScript errors

**Need help?**
Contact eva.de-quintana@es.abb.com
