<h2>Funcionalidades</h2>
<ul>
    <li><strong>Depositar</strong>: O usuário pode adicionar dinheiro ao saldo bancário.</li>
    <li><strong>Sacar</strong>: O usuário pode retirar dinheiro do saldo, sujeito a algumas regras:
        <ul>
            <li>O saque máximo por transação é R$500,00.</li>
            <li>O limite diário de saques é 3.</li>
            <li>O saldo deve ser suficiente para a transação.</li>
        </ul>
    </li>
    <li><strong>Extrato</strong>: Exibe o histórico de depósitos, saques e o saldo atual.</li>
    <li><strong>Sair</strong>: Finaliza o programa.</li>
</ul>

<h2>Como Executar o Programa</h2>
<ol>
    <li>Certifique-se de ter o Python instalado (versão 3.x).</li>
    <li>Execute o arquivo Python no terminal ou em um ambiente de desenvolvimento.</li>
    <li>Escolha uma opção do menu exibido.</li>
</ol>

<h2>Exemplo de Uso</h2>
<pre>
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
Digite a opção desejada: 1
Digite o valor que deseja depositar: 100
Seu saldo atual: R$100.00
</pre>
<h2>Estrutura do Código</h2>
<ul>
    <li><strong>Função <code>deposito(valor_deposito)</code></strong>: Adiciona dinheiro ao saldo, desde que o valor seja maior que zero.</li>
    <li><strong>Função <code>saque(valor_saque)</code></strong>: Permite ao usuário sacar dinheiro respeitando as regras estabelecidas.</li>
    <li><strong>Função <code>extrato()</code></strong>: Exibe os valores depositados, sacados e o saldo atual.</li>
    <li><strong>Loop Principal</strong>: Exibe o menu e permite ao usuário escolher a ação desejada.</li>
</ul>

<h2>Melhorias Possíveis</h2>
<ul>
    <li>Implementar um sistema de autenticação para usuários.</li>
    <li>Armazenar transações em um banco de dados.</li>
    <li>Criar uma interface gráfica para melhorar a experiência do usuário.</li>
</ul>

<hr>
<p>Este projeto é uma implementação básica de um sistema bancário para fins educacionais.</p>
