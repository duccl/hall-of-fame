let id_display_search = '#search_results'
let baseURLYoutubeWatchVideo = 'https://www.youtube.com/watch?v='
const callAPI = (text, callback) => {
    $.ajax({
        url: '/video/search',
        data: {
            'search_term': text
        },
        dataType: 'json'
    })
    .done(callback)
}

const callAddVideoPost = (event_fired) =>{
    $('#id_url').val(baseURLYoutubeWatchVideo + event_fired.target.id)
    $('#new_video').submit()
}

const build_youtube_iframe = (youtube_id) => {
    let iframe = document.createElement('iframe');
    iframe.width = '100%';
    iframe.height = '225';
    iframe.src = "https://www.youtube.com/embed/" + youtube_id
    iframe.frameborder="0";
    iframe.allow="accelerometer";   
    return iframe
}

const build_column_container = () => {
    let div = document.createElement('div')
    div.setAttribute('class', 'col-md-4 mt-3 margin-top-md roboto')
    div.style.color = 'black'
    return div
}

const build_card_container = () => {
    let div = document.createElement('div')
    div.setAttribute('class', 'card mb-4 shadow-sm')
    div.style.color = 'black'
    return div
}

const build_card_body = () => {
    let div = document.createElement('div')
    div.setAttribute('class', 'card-body')
    div.style.color = 'black'
    return div
}

const build_card_title = (title) => {
    let title_element = document.createElement('h5')
    title_element.setAttribute('class', 'card-title')
    title_element.style.color = 'black'
    title_element.innerHTML = title
    return title_element
}

const build_card_text = (description) => {
    let description_element = document.createElement('p')
    description_element.setAttribute('class', 'card-text text-truncate')
    description_element.style.color = 'black'
    description_element.innerHTML = description
    return description_element
}

const build_card_add_button = (youtube_id) =>{
    let button = document.createElement('button')
    button.setAttribute('class','btn btn-primary')
    button.innerText = 'Add Video'
    button.id = youtube_id
    button.onclick = callAddVideoPost
    return button;
}

const build_entire_youtube_video_content_element = (title,description,youtube_id) => {
    let container_div = build_column_container()
    let card_container = build_card_container()
    let card_youtube_video = build_youtube_iframe(youtube_id)
    let card_body = build_card_body()
    let card_title = build_card_title(title)
    let card_text = build_card_text(description)
    let card_add_video_button = build_card_add_button(youtube_id)
    card_body.appendChild(card_title)
    card_body.appendChild(card_text)
    card_body.appendChild(card_add_video_button)
    card_container.appendChild(card_youtube_video)
    card_container.appendChild(card_body)
    container_div.appendChild(card_container)
    return container_div
}

const populateSearchContainer = (data) => {
    $(id_display_search).text("")
    data['items'].map(item => {
        let video_snippet = item['snippet']
        let youtube_video_element = build_entire_youtube_video_content_element(video_snippet['title'],
                                                                               video_snippet['description'],
                                                                               item['id']['videoId'])
        $(id_display_search).append(youtube_video_element)
    })
}

let delayTimer;
$("#id_search_term").keyup(function () {
    clearTimeout(delayTimer);
    let search_text = $(this).val()
    $(id_display_search).text('Loading...')
    delayTimer = setTimeout(function () {
        callAPI(search_text, populateSearchContainer)
    }, 1000)
});