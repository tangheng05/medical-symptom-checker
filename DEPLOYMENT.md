# Vercel Deployment Guide

This guide explains how to deploy the Medical Symptom Checker to Vercel.

## Prerequisites

1. A [Vercel account](https://vercel.com/signup)
2. [Vercel CLI](https://vercel.com/cli) (optional, for command-line deployment)
3. Git repository with your code

## Project Structure for Vercel

```
medical-symptom-checker/
├── api/
│   └── index.py          # Serverless function entry point
├── data/
│   ├── diseases.json
│   └── recommendations.json
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── diagnosis_engine.py
│   └── recommendation_engine.py
├── app.py                # Flask application
├── config.py             # Configuration
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel configuration
└── .vercelignore         # Files to exclude from deployment
```

## Deployment Options

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to GitHub:**
   ```powershell
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Import to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`
   - Click "Deploy"

3. **Wait for deployment:**
   - Vercel will build and deploy your application
   - You'll get a live URL (e.g., `your-project.vercel.app`)

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```powershell
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```powershell
   vercel login
   ```

3. **Deploy:**
   ```powershell
   cd C:\Users\Draxler\Documents\Norton\NU_ExpertSystems\Y3S1\medical-symptom-checker
   vercel
   ```

4. **Follow the prompts:**
   - Set up and deploy: Yes
   - Which scope: Select your account
   - Link to existing project: No (first time) or Yes (redeployment)
   - Project name: Accept default or provide custom name
   - Directory: `.` (current directory)
   - Override settings: No

5. **Production deployment:**
   ```powershell
   vercel --prod
   ```

## Configuration Details

### vercel.json Explanation

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ],
  "env": {
    "FLASK_ENV": "production"
  }
}
```

- **builds**: Specifies that `api/index.py` is a Python serverless function
- **routes**: All requests are routed to the Flask app
- **env**: Sets production environment variable

## Troubleshooting Common Issues

### 500 Internal Server Error

**Possible causes:**
1. **Missing dependencies** - Check that all packages in `requirements.txt` are compatible
2. **File path issues** - Ensure data files are in the correct location
3. **Import errors** - Verify all modules can be imported correctly

**Solutions:**
- Check Vercel logs: Go to your project → Deployments → Click on deployment → View Function Logs
- Test locally first:
  ```powershell
  python app.py
  ```
- Verify file structure matches expected layout

### Static Files Not Loading

If CSS/JS files aren't loading:
1. Check that `static/` and `templates/` folders are committed to git
2. Verify paths in HTML use Flask's `url_for()`:
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   ```

### Data Files Not Found

If JSON files aren't loading:
1. Ensure `data/` folder is not in `.vercelignore`
2. Check that `data/` folder is committed to git
3. Verify paths in `config.py` use `Path` objects correctly

## Environment Variables (Optional)

If you need to set environment variables:

1. **Via Vercel Dashboard:**
   - Go to Project Settings → Environment Variables
   - Add variables like `SECRET_KEY`

2. **Via CLI:**
   ```powershell
   vercel env add SECRET_KEY
   ```

## Monitoring and Logs

- **View logs:** Project → Deployments → Function Logs
- **Monitor usage:** Project → Analytics
- **Error tracking:** Project → Deployments → Build Logs

## Domain Configuration (Optional)

To use a custom domain:
1. Go to Project Settings → Domains
2. Add your domain
3. Follow DNS configuration instructions

## Redeployment

Vercel automatically redeploys when you push to your GitHub repository:

```powershell
git add .
git commit -m "Update application"
git push origin main
```

Or manually redeploy:
```powershell
vercel --prod
```

## Performance Tips

1. **Cold starts:** First request may be slow (serverless warmup)
2. **Caching:** Data files are cached in memory after first load
3. **Region:** Vercel automatically deploys to multiple regions

## Support

- **Vercel Documentation:** https://vercel.com/docs
- **Vercel Support:** https://vercel.com/support
- **Flask Documentation:** https://flask.palletsprojects.com/

## Rollback

If a deployment has issues:
1. Go to Deployments
2. Find the previous working deployment
3. Click "..." → "Promote to Production"

