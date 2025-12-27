let dadosUltimaSimulacao = null;
let carroSelecionadoId = null;

const form = document.getElementById("reservaForm");
const mensagemNenhumCarro = document.getElementById("nenhumCarro");
const cards = document.querySelectorAll(".car-card");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const dadosParaAPI = {
        categoria_id: document.getElementById("categoria").value,
        agencia_id: document.getElementById("agencia").value,
        data_retirada: document.getElementById("retirada").value,
        data_devolucao: document.getElementById("devolucao").value
    };

    fetch("http://127.0.0.1:5000/simular_reserva", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosParaAPI)
    })
        .then(res => res.json())
        .then(dados => {
            dadosUltimaSimulacao = dados;
            carroSelecionadoId = null;

            mensagemNenhumCarro.classList.add("hidden");

            cards.forEach(card => {
                card.classList.add("hidden");
                card.classList.remove("selected", "flipped");
            });

            let encontrou = false;

            (dados.carros || []).forEach(carro => {
                if (!carro.disponivel) return;

                const card = document.querySelector(
                    `.car-card[data-carro-id="${carro.carro_id}"]`
                );

                if (!card) return;

                encontrou = true;
                card.classList.remove("hidden");

                card.querySelector("h4").textContent = carro.modelo;

            });

            if (!encontrou) {
                mensagemNenhumCarro.classList.remove("hidden");
            }
        })
        .catch(() => alert("Erro ao simular reserva."));
});

/* ================= BOTÃO "VER DETALHES" ================= */

cards.forEach(card => {
    const btnDetalhes = card.querySelector(".btn-detalhes");

    const btnAlugar = card.querySelector(".btn-alugar");

    // Flip APENAS no botão "Ver detalhes"
    btnDetalhes?.addEventListener("click", e => {
        e.stopPropagation();
        if (!dadosUltimaSimulacao) return;

        cards.forEach(c => c.classList.remove("selected", "flipped"));

        card.classList.add("selected", "flipped");
        carroSelecionadoId = card.dataset.carroId;

        preencherDadosNoCard(card);
    });

    // Clique no botão Alugar (não mexe no flip)
    btnAlugar?.addEventListener("click", e => {
        e.stopPropagation();
        alert("Carro alugado com sucesso! 🚗");
        // aqui você pode integrar com backend depois
    });
});

cards.forEach(card => {
    const btnVoltar = card.querySelector(".btn-voltar");

    btnVoltar?.addEventListener("click", e => {
        e.stopPropagation();
        card.classList.remove("selected", "flipped");
        carroSelecionadoId = null;
    });
});

/* ================= PREENCHER DADOS NO VERSO ================= */

function preencherDadosNoCard(card) {
    if (!dadosUltimaSimulacao) return;

    card.querySelector(".preco").textContent =
        `R$ ${Number(dadosUltimaSimulacao.tarifa_diaria)
            .toFixed(2)
            .replace(".", ",")} / dia`;

    card.querySelector(".diarias").textContent =
        `Diárias: ${dadosUltimaSimulacao.diarias}`;

    card.querySelector(".preco-final").textContent =
        `Total: R$ ${Number(dadosUltimaSimulacao.preco_final)
            .toFixed(2)
            .replace(".", ",")}`;
}
