import re
import full_scripts.site_map as sitemap
import full_scripts.define_ip as add
import full_scripts.whois_web as whois
import full_scripts.reverse_DNS as dns
import full_scripts.site_location as location
import full_scripts.dns_resolver as resolver
import full_scripts.site_ns_lookup as ns
import full_scripts.revers_ip_lookup as reverse_ip
import full_scripts.robots as robot
     
    
def menu_choice():
    [print(i[0]) for i in menu]
    try:
        while (num := int(input('\nEnter the option number: '))) \
                not in range(0, 11):
            print('Choose number from menu')
    except Exception as e:
        print('Error', e)
    else:
        item_choice(num)


def choose_target():
    try:
        if re.search(r'(?=:\/\/)?[\w\b.-]*\.\w{2,4}',
                     target := input('Enter target: ')).group():
            return target
    except Exception:
        print('Wrong input')


def item_choice(num):
    if num == 0:
        print('Program is complete!')
    elif num != 10:
        print('-' * 32, menu[int(num)][0], '-' * 32, sep='\n')
        menu[int(num)][1].my_func(choose_target())
        menu_choice()
    else:
        all_items()


def all_items():
    print('-' * 32, menu[10][0], '-' * 32, sep='\n')
    with open('check_domain.txt', 'w') as f:
        f.write(envelope)
        target = choose_target()
        for item in menu[1:10]:
            f.write(str(f"{'-' * 32}\n{item[0]}\n{'-' * 32}") + '\n')
            f.write(str(item[1].my_func(target, write=True)) +'\n')
        print('Done!')
    menu_choice()
    

if __name__ == '__main__':
    envelope = '''
██╗  ██╗██╗   ██╗███╗   ██╗██████╗ 
██║  ██║██║   ██║████╗  ██║██╔══██╗
███████║██║   ██║██╔██╗ ██║██║  ██║
██╔══██║██║   ██║██║╚██╗██║██║  ██║
██║  ██║╚██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
           OSINT BOX by StripedBear                  \n'''
    
    menu = [('\n\033[35m0. Exit the program',), ('1. Host IP', add),
            ('2. Site location', location), ('3. Whois', whois),
            ('4. NsLookup', ns), ('5. DNS MX-Record', resolver),
            ('6. Reverse DNS', dns), ('7. robots.txt', robot),
            ('8. Sitemap', sitemap), ('9. Reverse IP Lookup', reverse_ip),
            ('10. Save all items to file\033[0m',)]
    
    print(f'\033[35m{envelope}\033[0m')
    menu_choice()
