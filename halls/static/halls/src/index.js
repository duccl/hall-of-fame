let id_display_search = '#search_results'
const callAPI = async (text, callback) => {
    await $.ajax({
        url: '/video/search',
        data: {
            'search_term': text
        },
        dataType: 'json'
    })
    .done(callback)
}

const populateSearchContainer =  (data) => {
    console.log(data['items'])
    data['items'].map(item=>{
        let video_snippet = item['snippet']
        let div = document.createElement('div')
        div.setAttribute('class','card row margin-top-md roboto')
        div.innerHTML = `${video_snippet['title']} \r\n
                         ${video_snippet['description']}`
        div.style.color= 'black'
        $(id_display_search).append(div)
    })
}

let delayTimer;
$("#id_search_term").keyup(function(){
    clearTimeout(delayTimer);
    let search_text = $(this).val()
    $(id_display_search).text('Loading...')
    delayTimer = setTimeout(function(){
        callAPI(search_text,populateSearchContainer)
    },1000)
});