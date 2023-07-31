window.Telegram.WebApp.ready();
window.Telegram.WebApp.expand();

document.querySelectorAll('.card').forEach(card => {
    const characterId = card.getAttribute('data-character-id');
    card.addEventListener('click', () => sendData(characterId));
});

function sendData(characterId) {
    fetch(`/ai/set-character?character_id=${characterId}&user_id=${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
});
    
    // const data = {
    //     user_id: window.Telegram.WebApp.initDataUnsafe.user.id,
    //     character_id: characterId
    // };

    // const options = {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(data)
    // };

    // fetch(`/ai/set-character`, options)
    //     .then(response => {
    //         if (response.ok) {
    //             console.log('Данные успешно отправлены на сервер.');
    //         } else {
    //             console.error('Ошибка при отправке данных на сервер:', response.status);
    //         }
    //     })
    //     .catch(error => {
    //         console.error('Ошибка при выполнении запроса:', error);
    //     });
    window.Telegram.WebApp.close()
}

