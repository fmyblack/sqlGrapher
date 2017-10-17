select
'${DP_1_DAYS_AGO_Ymd}',
m.kdt_id,
m.tag_id,
m.fans_uv as all_fans_uv,
m.add_fans_uv,
m.buyer_uv,
m.new_buyer_uv,
n.rule_name
from
(
	select
	if(x.kdt_id is not NULL,x.kdt_id,y.kdt_id) as kdt_id,
	if(x.tag_id is not NULL,x.tag_id,y.tag_id) as tag_id,
	if(x.fans_uv is not NULL,x.fans_uv,0) as fans_uv,
	if(x.new_fans_uv is not NULL,x.new_fans_uv - x.gone_fans_uv,0) as add_fans_uv,
	if(y.buyer_uv is not NULL,y.buyer_uv,0) as buyer_uv,
	if(y.new_buyer_uv is not NULL,y.new_buyer_uv,0) as new_buyer_uv
	from
	(
		select
		d.kdt_id,
		c.tag_id,
		count(distinct c.fans_id) as fans_uv,
		count(distinct if(                      FROM_UNIXTIME(unix_timestamp(follow_time)   , 'yyyyMMdd') = '${DP_1_DAYS_AGO_Ymd}' , c.fans_id , NULL)) as new_fans_uv ,
		count(distinct if( is_subscribe = 0 AND FROM_UNIXTIME(unix_timestamp(unfollow_time), 'yyyyMMdd') = '${DP_1_DAYS_AGO_Ymd}' , c.fans_id , NULL)) as gone_fans_uv
		from
		(
			select
			a.mp_id,
			a.tag_id,
			a.fans_id,
            b.follow_time as follow_time,
            b.unfollow_time as unfollow_time,
			if(b.is_subscribe is not NULL,is_subscribe,2) as is_subscribe
			from
			(
				select mp_id,tag_id,fans_id from ods.scrm_fans_tag where fans_id > 0 and mp_id > 0 and tag_id > 0
			) a left outer join
			(
                select 
                    fans_id,
                    is_fans as is_subscribe,
                    follow_time,
                    unfollow_time
                from 
                    ods.acct_wechat_fans 
                where 
                        FROM_UNIXTIME(unix_timestamp(follow_time), 'yyyyMMdd') = '${DP_1_DAYS_AGO_Ymd}'
                    OR
                        FROM_UNIXTIME(unix_timestamp(unfollow_time), 'yyyyMMdd') = '${DP_1_DAYS_AGO_Ymd}'
			) b on a.fans_id = b.fans_id
		) c join (select kdt_id, min(mp_id) as mp_id from ods.team_user_mp where kdt_id > 0 group by kdt_id) d on c.mp_id = d.mp_id
		group by d.kdt_id,c.tag_id
	) x full outer join
	(
		SELECT 
		a.kdt_id,
		a.tag_id,
		count(distinct a.buyer_id) as buyer_uv,
		count(distinct b.buyer_id) as new_buyer_uv
		from 
		(
			select kdt_id,tag_id,buyer_id from ods.scrm_buyer_tag where buyer_id > 0 and kdt_id > 0
		) a left outer join 
		(
			select kdt_id,buyer_id from ods.scrm_buyer_fans where par = '${DP_1_DAYS_AGO_Ymd}'
		) b on a.kdt_id = b.kdt_id and a.buyer_id = b.buyer_id
		group by a.kdt_id,a.tag_id
	) y on x.kdt_id = y.kdt_id and x.tag_id = y.tag_id
) m join ods.scrm_fans_rule n
on m.tag_id = n.id