mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
headless = trye\n\
\n\
" > ~/.streamlit/config.toml
