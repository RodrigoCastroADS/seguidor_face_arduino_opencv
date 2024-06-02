# seguidor_face_arduino_opencv
 Face Tracking com Arduino e OpenCV
Este projeto é uma aplicação de rastreamento facial utilizando OpenCV em Python e controle de servomotores com Arduino. O programa detecta rostos em tempo real através da webcam e move os servomotores para acompanhar o movimento do rosto.

Instalação
Certifique-se de ter o Python 3.10 instalado. Você pode baixá-lo em [python.org](https://www.npackd.org/p/org.python.Python64/3.10.1) .

Instale as bibliotecas necessárias usando o pip:

bash
Copy code
pip install pyfirmata mediapipe opencv-python
Conecte o Arduino ao computador e carregue o programa StandardFirmata ou similar no Arduino.

Como Funciona
Abra o arquivo seguidor_face_arduino_opencv.py em um editor de texto ou IDE Python.

Conecte a placa Arduino ao computador através da porta USB.

Execute o script Python:

bash
Copy code
pythonseguidor_face_arduino_opencv.py
A webcam será ativada e o programa começará a rastrear rostos em tempo real.

O programa moverá os servomotores horizontal e verticalmente para manter o rosto no centro da imagem da webcam.

Pressione a tecla 'q' para fechar a aplicação e liberar a webcam.

Contribuição
Sinta-se à vontade para contribuir com melhorias neste projeto. Basta seguir estas etapas:

Faça um fork do repositório.

Crie uma nova branch (git checkout -b feature/nova-funcionalidade).

Faça commit das suas alterações (git commit -am 'Adicionar nova funcionalidade').

Envie suas alterações para o repositório remoto (git push origin feature/nova-funcionalidade).

Crie um novo Pull Request.

Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.
