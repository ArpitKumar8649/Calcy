#!/bin/bash
# Prepare files for Hugging Face Spaces deployment

echo "🚀 Preparing TalentScout for Hugging Face Spaces..."
echo ""

# Create a deployment folder
DEPLOY_DIR="/app/hf_deployment"
rm -rf $DEPLOY_DIR
mkdir -p $DEPLOY_DIR

# Copy main app files
echo "📦 Copying main application files..."
cp /app/streamlit_app.py $DEPLOY_DIR/
cp /app/requirements.txt $DEPLOY_DIR/
cp /app/README.md $DEPLOY_DIR/

# Copy configuration folders
echo "📁 Copying configuration folders..."
cp -r /app/config $DEPLOY_DIR/
cp -r /app/services $DEPLOY_DIR/
cp -r /app/utils $DEPLOY_DIR/
cp -r /app/components $DEPLOY_DIR/
cp -r /app/.streamlit $DEPLOY_DIR/

# Create .gitignore for the deployment
echo "📝 Creating .gitignore..."
cat > $DEPLOY_DIR/.gitignore << 'EOF'
__pycache__/
*.py[cod]
*$py.class
.env
.env.streamlit
*.log
.DS_Store
EOF

echo ""
echo "✅ Files prepared in: $DEPLOY_DIR"
echo ""
echo "📋 Directory structure:"
tree -L 2 $DEPLOY_DIR 2>/dev/null || find $DEPLOY_DIR -type f -o -type d | head -20
echo ""
echo "📌 Next steps:"
echo "   1. Go to https://huggingface.co/new-space"
echo "   2. Create a new Space with Streamlit SDK"
echo "   3. Upload all files from: $DEPLOY_DIR"
echo "   4. Configure secrets in Space settings"
echo ""
echo "📖 Full guide: /app/DEPLOYMENT_GUIDE.md"
