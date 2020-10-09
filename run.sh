python generate_plots.py
echo "[telegram]" >> telegram-send.conf
echo "token = $token" >> telegram-send.conf
echo "chat_id = $chat_id" >> telegram-send.conf
telegram-send --config telegram-send.conf -i andamento_nazionale_1.png andamento_nazionale_2.png andamento_torino.png
