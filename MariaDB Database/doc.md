Problemas e Soluções
Durante o processo de desenvolvimento e configuração do ambiente para conectar SQLAlchemy ao MariaDB, foram identificados diversos problemas. Abaixo estão detalhados cada problema específico e as soluções implementadas para corrigi-los:

Problema 1: Erro de Codificação de Senha com o Símbolo "@"
Descrição do Problema: SQLAlchemy estava encontrando erros de conexão devido ao símbolo "@" presente na senha do banco de dados (Gremio9@).

Explicação: O símbolo "@" possui significado especial em URLs e strings de conexão, sendo utilizado para separar credenciais de usuário (username:password) do host (@host). Isso resultava na interpretação incorreta do símbolo "@" em Gremio9@ como parte do host ou usuário, levando a falhas na conexão.

Solução Implementada: Para resolver este problema, a senha Gremio9@ foi corretamente codificada para Gremio9%40, onde %40 é a forma codificada URL do "@".

Implementação: A versão corrigida (Gremio9%40) foi utilizada no URL de conexão do SQLAlchemy (mysql+pymysql://root:Gremio9%40@127.0.0.1:3306/users) para garantir a interpretação e autenticação corretas durante as tentativas de conexão.

Problema 2: Erro de Configuração de Tabela no Banco de Dados
Descrição do Problema: Após estabelecer a conexão com sucesso, foi detectado um erro relacionado à descrição da estrutura da tabela unisinos.

Explicação: O SQLAlchemy tentou acessar uma coluna id que não estava definida na estrutura da tabela unisinos, resultando em um erro de "Unknown column".

Solução Implementada: Era necessário atualizar a estrutura da tabela unisinos para incluir todas as colunas necessárias conforme definido no modelo SQLAlchemy.

Implementação: A estrutura da tabela unisinos foi ajustada para incluir corretamente todas as colunas necessárias (id INTEGER, first_name CHAR(50), last_name CHAR(50), Idade INTEGER), garantindo assim que as consultas realizadas pelo SQLAlchemy correspondessem à estrutura esperada.

Problema 3: Erro de Sintaxe SQL na Consulta Gerada pelo SQLAlchemy
Descrição do Problema: Após corrigir a estrutura da tabela unisinos, ocorreu um erro de "Unknown column" relacionado à coluna last_name na consulta gerada pelo SQLAlchemy.

Explicação: O SQLAlchemy gerou uma consulta SQL que referenciava uma coluna last_name que não existia na tabela unisinos, devido à diferença entre a estrutura da tabela e a consulta solicitada.

Solução Implementada: Foi necessário ajustar a consulta gerada pelo SQLAlchemy para corresponder exatamente à estrutura atualizada da tabela unisinos.

Implementação: A consulta SQL foi corrigida para selecionar apenas as colunas existentes na tabela unisinos (id, first_name, Idade), garantindo assim que a operação de consulta fosse executada corretamente sem erros de sintaxe.

Conclusão
Cada problema identificado durante a configuração e utilização do SQLAlchemy com MariaDB foi abordado de maneira sistemática e resolvido com sucesso através das soluções implementadas. A codificação correta da senha, atualização da estrutura da tabela e correção da sintaxe da consulta SQL foram essenciais para garantir a funcionalidade adequada e a integração bem-sucedida entre SQLAlchemy e MariaDB. Essas experiências proporcionaram aprendizados valiosos sobre o manuseio de caracteres especiais em URLs e a importância da consistência entre a estrutura do banco de dados e as consultas executadas pelo ORM.

Este relatório resume as etapas de diagnóstico, solução e implementação necessárias para superar os desafios encontrados, destacando a importância da compreensão detalhada das ferramentas utilizadas e das melhores práticas para garantir a eficiência e a confiabilidade no desenvolvimento de aplicações com SQLAlchemy e bancos de dados MariaDB.