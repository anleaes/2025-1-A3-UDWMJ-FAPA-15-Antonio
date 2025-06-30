# SISVAC - Sistema de Vacinação

## Configuração do Ambiente

### 1. Clone o repositório
```bash
git clone [url-do-repositorio]
cd 2025-1-A3-UDWMJ-FAPA-15-Antonio
```

### 2. Configuração das Variáveis de Ambiente

> O arquivo `.env` é lido automaticamente pelo python-decouple. Basta garantir que ele esteja na raiz do projeto. Não é necessário importar ou chamar manualmente no código.

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```bash
cp .env.example .env
```

Configure as seguintes variáveis no arquivo `.env`:

```env
# Configuração do banco de dados Oracle
DB_ENGINE=django.db.backends.oracle
DB_NAME=seu_banco_de_dados
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_WALLET_LOCATION=C:\ORACLE\Wallet_SeuWallet
DB_WALLET_PASSWORD=senha_do_wallet

# Configuração do Django
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
```

### 3. Instalação das Dependências

```bash
pip install -r requirements.txt
```

### 4. Configuração do Banco Oracle

Certifique-se de que:
- O Oracle Instant Client está instalado
- O wallet do banco está configurado no caminho especificado em `DB_WALLET_LOCATION`
- A variável de ambiente `TNS_ADMIN` aponta para o wallet

### 5. Migrações do Banco

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Executar o Servidor

```bash
python manage.py runserver
```

## Estrutura do Projeto

- `apps/` - Aplicações Django (clinic, person, vaccine, etc.)
- `templates/` - Templates HTML
- `static/` - Arquivos estáticos (CSS, JS, imagens)
- `sisvacapp/` - Configurações principais do Django

## Segurança

⚠️ **IMPORTANTE**: 
- Nunca faça commit do arquivo `.env` 
- Use o arquivo `.env.example` para documentar as variáveis necessárias
- Em produção, configure as variáveis de ambiente diretamente no servidor