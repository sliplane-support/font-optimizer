# Font Optimizer

Convert ttf fonts to woff2 and remove all glyphs that you don't need. You can 10x downsize ttf font files this way. The repo contains

- a bash script "font-optimizer.sh" to optimize fonts locally
- Basic code for a Python web app to run the optimizer with a GUI
- Dockerfile to simply deploy the code

## Using the Bash script

The script file needs execute permissions:

```bash
chmod +x font-optimizer.sh
```

It accepts one parameter, which is the path to the ttf file. Use it like this:

```bash
./font-optimizer.sh your-font.ttf
```

The result will be a `your-font.woff2` file, with a limited character set.

To change, what characters will be included, update the unicodes param in the script.

## Using the python web app

You can follow the instructions from the `Dockerfile`.

Make sure you have python 3.12 installed.

Install dependencies with 

```bash
pip install -r requirements.txt
```

Start the app by running 

```bash
python app.py
```

You can access the web interface on `http://localhost:5000`

## Docker

Build the Docker image:

```bash
docker build . -t font-optimizer
```

Run the image:
```bash
docker run -p 5000:5000 font-optimizer
```

You can access the web interface on `http://localhost:5000`

## Deploy the webapp

You can use [Sliplane](https://sliplane.io) to deploy the webapp. 

1. Fork the repo
2. Login at Sliplane with your GitHub account and allow access to the forked repo 
3. Inside a project, click "Deploy Service" and choose a server to deploy to
4. Choose repository as a deploy source
5. Select the repository from the dropdown, keep the default settings and hit "Deploy"


## Credits

Thanks to [mrflix](https://github.com/mrflix) for sharing the bash script.

Checkout [Sliplane](sliplane.io) for a simple way to deploy containerized apps.