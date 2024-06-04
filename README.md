# streamlit_demo
## Running streamlit
### Running your application
`streamlit run app.py`

### Running your application as a Python module
`python -m streamlit run your_script.py`

### Running your application via URL
`streamlit run https://{...}/url_link_your_script.py`

## Setting up your application
### Adding a Secrets file
Streamlit supports a global secrets file specified in the user's home directory, such as ~/.streamlit/secrets.toml
![image](https://github.com/tagaretiro/streamlit_demo/assets/63424036/f97d68a0-e917-4904-9484-9b62085f3cf4)

### Adding a Configuration file
To define your configuration add a config file to your working directory. ~/.streamlit/config.toml
![image](https://github.com/tagaretiro/streamlit_demo/assets/63424036/392813be-37e5-4007-9709-6f6d25724a90)

To see all configuration options available you can use the following command
`streamlit config show`
