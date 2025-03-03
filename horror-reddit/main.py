from horrorRedditImg import make_url_list, get_image_list, make_individual_reel

def main(number):
    print('starting...')
    
    URL_list = make_url_list()
    print('list of urls')
    
    check = get_image_list(URL_list, number)
    print('received images')
    
    make_individual_reel(number, check)
    print(f'made {number} videos')
    print('example title: r/twosentenceHorror #shorts #horror #scary #creepy #twosentencehorrorstories #creepypastas')

if __name__ == '__main__':
    main(5)   