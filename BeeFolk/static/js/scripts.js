window.addEventListener('DOMContentLoaded', () => {
    // Controle de rolagem para a barra de navegação
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;

    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if (currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove('is-visible');
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });

    // Submissão AJAX do formulário de calculadora
    const form = document.getElementById('calculator-form');

    if (form) { // Verifica se o formulário existe na página
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Previne o comportamento padrão do formulário

            const formData = new FormData(form); // Captura os dados do formulário
            
            fetch('/calculator', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text()) // Obtém a resposta como texto HTML
            .then(html => {
                // Atualiza a área de resultado com o retorno do Flask
                document.getElementById('result-container').innerHTML = html;
            })
            .catch(error => console.error('Erro:', error));
        });
    }

    // Navegação entre seções de calculadora
    const navButtons = document.querySelectorAll('.nav-button');

    navButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); // Previne o comportamento padrão do link

            // Remove a classe 'active' de todas as seções
            document.querySelectorAll('.calculator-section-content').forEach(section => {
                section.classList.remove('active');
            });

            // Adiciona a classe 'active' à seção alvo
            const targetSelector = this.getAttribute('data-target');
            const targetSection = document.querySelector(targetSelector);
            if (targetSection) {
                targetSection.classList.add('active');
            }
        });
    });

    // Exibe a seção inicial
    document.querySelector('#abv_calc').classList.add('active');
});
