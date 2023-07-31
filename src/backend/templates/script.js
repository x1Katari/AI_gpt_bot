window.Telegram.WebApp.ready();
window.Telegram.WebApp.expand();

document.querySelectorAll('.card').forEach(card => {
    const characterId = card.getAttribute('data-character-id');
    card.addEventListener('click', () => sendData(characterId));
});

function sendData(characterId) {
    fetch(`/set-character?character_id=${characterId}&user_id=${window.Telegram.WebApp.initDataUnsafe.user.id}`, {
      method: 'POST',
      // headers: {
      //   'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      //   'Connection': 'keep-alive',
      //   'Content-Length': '0',
      //   'Origin': 'http://127.0.0.1:8001',
      //   'Referer': 'http://127.0.0.1:8001/docs',
      //   'Sec-Fetch-Dest': 'empty',
      //   'Sec-Fetch-Mode': 'cors',
      //   'Sec-Fetch-Site': 'same-origin',
      //   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
      //   'accept': 'application/json',
      //   'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
      //   'sec-ch-ua-mobile': '?0',
      //   'sec-ch-ua-platform': '"macOS"'
      // }
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

