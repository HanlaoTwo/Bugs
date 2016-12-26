[PRO*C结果集语句][select *
                    from (select sendercomp_id, user_id, company_id, businsys_no, busin_account,worth_value,asset,today_income_ratio,week_income_ratio,month_income_ratio,year_income_ratio, income_ratio, position_str
                            from combusincomeratio a
                           where sendercomp_id = @sendercomp_id
                             and company_id = @company_id
                           order by @oder_type,a.position_str asc)
                  where rownum <= @request_num][combusincomeratio]
             
                   
  {
    [PRO*C结果集返回]
  }
  else
  {
    [PRO*C函数报错返回][ERR_COM_QRY_COMBUSINCOMERATIO_FAIL][查询账户收益率信息表失败][@sendercomp_id,@company_id]
  }


  and position_str > @position_str




  select *
    from(
            select b.*, b.rownum as position_str
             from (
                        select sendercomp_id, user_id, company_id, businsys_no, busin_account,worth_value,asset,today_income_ratio,week_income_ratio,month_income_ratio,year_income_ratio, income_ratio
                            from combusincomeratio a
                           where sendercomp_id = @sendercomp_id
                             and company_id = @company_id
                           order by @oder_type desc
                    ) b
            where rownum <= (@request_num + to_number(@position_str))
        )
   where position_str > to_number(@position_str)



 select init_date, user_id, money_type, profit_type, profit_balance, position_str
      from (select init_date, user_id, money_type,  profit_type, profit_balance, rownum as position_str
              from (select init_date, user_id, money_type, profit_type,
                           sum(profit_balance) as profit_balance, max(position_str) as position
                      from hs_his.his_comuncomeprofit
                     where user_id = @user_id
                       and sendercomp_id = @sendercomp_id
                       and (money_type = @money_type or trim(@money_type) is null)
                       and init_date >= @begin_date  
                       and init_date <= @end_date
                     group by init_date, user_id, money_type, profit_type
                     order by position desc) 
             where rownum <= (@request_num + to_number(@position_str))) 
     where position_str > to_number(@position_str)][hs_his.his_comuncomeprofit]



     -------------------------------------------------------------------------------------------
      hs_snprintf(@sSql, 16000,"%s \n %s", @sSql, " select * from ( ");
 hs_snprintf(@sSql, 16000,"%s \n %s", @sSql, "select sendercomp_id, user_id, company_id, businsys_no, busin_account,worth_value,asset,today_income_ratio,week_income_ratio,month_income_ratio,year_income_ratio, income_ratio, position_str");
 hs_snprintf(@sSql, 16000,"%s \n %s", @sSql, " from combusincomeratio a");
 hs_snprintf(@sSql, 16000,"%s \n %s%s%s", @sSql, " where sendercomp_id = '",@sendercomp_id,"'");
 hs_snprintf(@sSql, 16000,"%s \n %s%s%s", @sSql, " and company_id = '",@company_id ,"'");
 hs_snprintf(@sSql, 16000,"%s \n %s%s%s", @sSql, " and position_str > '",@position_str ,"'");
 hs_snprintf(@sSql, 16000,"%s \n %s%s%s", @sSql, " order by ",@oder_type,",a.position_str asc)");
 hs_snprintf(@sSql, 16000,"%s \n %s%d%s", @sSql, " where rownum <= '",@request_num ,"'");
 ------------------------------------------------------------------------------------------------------



 select * from (  
                select *,rownum as position_str from (  
                                select sendercomp_id, user_id, company_id, businsys_no, busin_account,worth_value,asset,today_income_ratio,week_income_ratio,month_income_ratio,year_income_ratio, income_ratio, position_str 
                                    from combusincomeratio a 
                                    where sendercomp_id = '91036' 
                                    and company_id = '91000' 
                                    order by a.income_ratio desc ) b 
                where rownum <= (5+to_number(0))) 
  where position_str > to_number('0')