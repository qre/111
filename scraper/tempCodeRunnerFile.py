            # match_details_name = driver.find_element(By.XPATH, '//*[@id="col-content"]/h1')
            # print("name:", match_details_name.text)
            # match_details_time = driver.find_element(By.XPATH, '//*[@id="col-content"]/p[1]')
            # print("time: ", match_details_time.text)



            # if first_odds + payout >= 98:
            #     #matches98[match_details_name.text] = match_details_time.text, first_odds+payout
            #     matches98['players'] =  match_details_name.text
            #     matches98['time'] =  match_details_time.text
            #     matches98['payout+odds'] =  first_odds+payout
            # if second_odds + payout >= 98:
            #     #matches98[match_details_name.text] = match_details_time.text, second_odds+payout
            #     matches98['players'] =  match_details_name.text
            #     matches98['time'] =  match_details_time.text
            #     matches98['payout+odds'] =  second_odds+payout
            
            # # matches98_unique = [{'players': key, 'payout+odds': max(item['payout+odds'] for item in values)}
            # #      for key, values in groupby(matches98, lambda dct: dct['players'])]
            
            # def WriteJson(matches98, f):
            #     j = json.dumps(matches98)
            #     f.write(j)
            #     f.write(',')
            #     f.write('\n')

            # with open('File.json', 'a', buffering=1) as f:
            #     WriteJson(matches98, f)