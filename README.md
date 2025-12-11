<h1 align="center">🔍 Port Scanner</h1>

<p align="center">
    <strong>Um scanner de portas rápido, simples e eficiente desenvolvido em Python.</strong><br>
    Capaz de realizar varreduras completas (1–65535) ou apenas nas portas mais comuns.
</p>

<hr>

<h2>🚀 Funcionalidades</h2>

<ul>
    <li>Scan <strong>Full</strong> — 65.535 portas.</li>
    <li>Scan <strong>Common</strong> — portas mais utilizadas em serviços reais.</li>
    <li>Banner estilizado com <code>pyfiglet</code>.</li>
    <li>Saída colorida usando <code>colorama</code>.</li>
    <li>Argumentos via CLI com <code>argparse</code>.</li>
</ul>

<hr>

<h2>📦 Tecnologias Utilizadas</h2>

<ul>
    <li>Python 3+</li>
    <li><code>socket</code></li>
    <li><code>pyfiglet</code></li>
    <li><code>argparse</code></li>
    <li><code>colorama</code></li>
</ul>

<hr>

<h2>📥 Instalação</h2>

<h3>1. Clone o repositório</h3>

<pre><code>git clone https://github.com/Wevertonf45/port-scanner.git
cd port-scanner
</code></pre>

<h3>2. Instale as dependências</h3>

<pre><code>pip install -r requirements.txt
</code></pre>

<p><em>Caso não exista o arquivo <code>requirements.txt</code>, as dependências são:</em><br>
<code>pip install pyfiglet colorama</code>
</p>

<hr>

<h2>▶️ Como Usar</h2>

<h3>Scan comum (default)</h3>

<pre><code>python3 port-scanner.py -H 192.168.0.10
</code></pre>

<h3>Scan completo</h3>

<pre><code>python scanner.py -H 192.168.0.10 -m full
</code></pre>

<h3>Exemplo usando domínio</h3>

<pre><code>python scanner.py -H google.com -m common
</code></pre>

<hr>

<h2>🧠 Parâmetros Disponíveis</h2>

<table>
    <tr>
        <th>Parâmetro</th>
        <th>Descrição</th>
    </tr>
    <tr>
        <td><code>-H</code>, <code>--host</code></td>
        <td>Host ou IP alvo (obrigatório)</td>
    </tr>
    <tr>
        <td><code>-m</code>, <code>--mode</code></td>
        <td>Modo de varredura: <code>common</code> (padrão) ou <code>full</code></td>
    </tr>
</table>

<hr>

<h2>📜 Estrutura das Funções</h2>

<h3><code>scann_port(host, port)</code></h3>
<p>Testa se uma porta está aberta retornando <code>True</code> ou <code>False</code>.</p>

<h3><code>scan_range(host)</code></h3>
<p>Escaneia todas as portas de <code>1 a 65535</code>.</p>

<h3><code>scann_common_ports(host)</code></h3>
<p>Escaneia apenas a lista de portas comuns definidas no script.</p>

<hr>

<h2>⚠️ Aviso Legal</h2>

<p>
Este scanner deve ser usado <strong>somente</strong> em redes e dispositivos nos quais você possui permissão explícita.  
O uso indevido pode ser considerado atividade ilegal.
</p>

<hr>

<h2>👨‍💻 Autor</h2>

<p>
Feito por <strong>Weverton</strong><br>
GitHub: <a href="https://github.com/Wevertonf45">github.com/Wevertonf45</a>
</p>

<hr>

<h2>⭐ Contribua</h2>
<p>Pull requests são bem-vindos! Se gostou do projeto, deixe uma ⭐ no repositório 😄</p>
