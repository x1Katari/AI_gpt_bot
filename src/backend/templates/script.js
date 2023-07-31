window.Telegram.WebApp.ready();
window.Telegram.WebApp.expand();

document.querySelectorAll('.card').forEach(card => {
    const characterId = card.getAttribute('data-character-id');
    card.addEventListener('click', () => sendData(characterId));
});

// Обработка данных от бота при запуске приложения
const initData = window.Telegram.WebApp.initData

let user_id;

// Функция для отправки данных на сервер
function sendData(characterId) {
    const data = {
        user_id: user_id,
        character_id: characterId
    };

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch('/ai/set-character', options)
        .then(response => {
            if (response.ok) {
                console.log('Данные успешно отправлены на сервер.');
            } else {
                console.error('Ошибка при отправке данных на сервер:', response.status);
            }
        })
        .catch(error => {
            console.error('Ошибка при выполнении запроса:', error);
        });
}

if (initData) {
    const userData = JSON.parse(initData); // Парсим JSON-строку в объект
    user_id = userData.from_user.id;

    // Добавляем обработчики клика на карточки
    document.querySelectorAll('.card').forEach(card => {
        const characterId = card.getAttribute('data-character-id');
        card.addEventListener('click', () => sendData(characterId));
    });
}

