import requests
from dotenv import load_dotenv
from os import getenv
from os.path import join
from os import getcwd
import random
from os import remove


def get_url_for_upload_comic(access_token, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': group_id,
        'v': 5.92,
        'access_token': access_token
    }
    response = requests.get(url, params=params).json()
    return response['response']['upload_url']


def upload_comics_to_server(url_for_upload, filename):
    files = {'photo': open(filename, 'rb')}
    response = requests.post(url_for_upload, files=files).json()
    return response


def save_comics_in_group_album(access_token, group_id, info_for_save):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': group_id,
        'v': 5.92,
        'access_token': access_token,
        'server': info_for_save['server'],
        'photo': info_for_save['photo'],
        'hash': info_for_save['hash']
    }
    response = requests.post(url, params=params).json()
    info_for_publishing = response['response'][0]
    return info_for_publishing


def publishing_comic_in_group(access_token, group_id, info_for_publishing, description):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'owner_id': (-1)*int(group_id),
        'v': 5.92,
        'access_token': access_token,
        'from_group': 1,
        'message': description,
        'attachments': 'photo{owner_id}_{media_id}'.format(
            owner_id=info_for_publishing['owner_id'],
            media_id=info_for_publishing['id']
        )

    }
    requests.post(url, params)


def fetch_comic():
    number_of_comics = requests.get('http://xkcd.com/info.0.json').json()['num']
    num_of_comic = random.randint(1, number_of_comics)
    filename = 'comic{}.png'.format(num_of_comic)
    url = 'http://xkcd.com/{}/info.0.json'.format(num_of_comic)
    response = requests.get(url).json()
    image_url = response['img']
    description = response['alt']
    img_response = requests.get(image_url)
    with open(filename, 'wb') as file:
        file.write(img_response.content)
    return filename, description


def main():
    env_path = join(getcwd(), '.env')
    load_dotenv(env_path)

    access_token = getenv('ACCESS_TOKEN')
    group_id = getenv('GROUP_ID')

    filename, comic_description = fetch_comic()
    url_server_for_upload_comics = get_url_for_upload_comic(access_token, group_id)
    info_for_save = upload_comics_to_server(url_server_for_upload_comics, filename)
    info_for_publishing = save_comics_in_group_album(access_token, group_id, info_for_save)
    publishing_comic_in_group(access_token, group_id, info_for_publishing, comic_description)
    remove(join(getcwd(), filename))


if __name__ == '__main__':
    main()
