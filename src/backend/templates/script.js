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
    window.Telegram.WebApp.close()
}

