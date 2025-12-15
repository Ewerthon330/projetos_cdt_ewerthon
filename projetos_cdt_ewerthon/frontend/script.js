document.getElementById("reservaForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const categoria_id = document.getElementById("categoria").value;
    const agencia_id = document.getElementById("agencia").value;
    const data_retirada = document.getElementById("retirada").value;
    const data_devolucao = document.getElementById("devolucao").value;

    const dadosParaAPI = {
        categoria_id,
        agencia_id,
        data_retirada,
        data_devolucao
    };

    fetch("http://127.0.0.1:5000/simular_reserva", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dadosParaAPI)
    })
        .then(res => res.json())
        .then(dados => {
            if (dados.erro) {
                alert(dados.erro);
                return;
            }

            // =============================
            // RESULTADO DE PREÇO
            // =============================
            document.getElementById("diarias").textContent = dados.diarias;
            document.getElementById("precoBruto").textContent =
                dados.preco_bruto.toFixed(2).replace(".", ",");
            document.getElementById("precoFinal").textContent =
                dados.preco_final.toFixed(2).replace(".", ",");

            const listaFatores = document.getElementById("fatoresLista");
            listaFatores.innerHTML = "";
            dados.fatores_aplicados.forEach(f => {
                const li = document.createElement("li");
                li.textContent = f;
                listaFatores.appendChild(li);
            });

            document.getElementById("resultado").style.display = "block";

            // =============================
            // FILTRAR CARROS DISPONÍVEIS
            // =============================

            const cards = document.querySelectorAll(".car-card");

            // 1️⃣ Esconder todos os cards
            cards.forEach(card => {
                card.classList.add("hidden");
                card.classList.remove("indisponivel");
            });

            // 2️⃣ Mostrar apenas os disponíveis retornados pela API
            dados.carros.forEach(carro => {
                if (!carro.disponivel) return;

                const card = document.querySelector(
                    `.car-card[data-carro-id="${carro.carro_id}"]`
                );

                if (!card) return;

                card.classList.remove("hidden");

                // Atualiza preço visual
                const precoEl = card.querySelector(".preco");
                if (precoEl) {
                    precoEl.textContent = `R$ ${dados.tarifa_diaria
                        .toFixed(2)
                        .replace(".", ",")} / dia`;
                }
            });
        })
        .catch(err => {
            console.error(err);
            alert("Erro ao simular reserva.");
        });
});
