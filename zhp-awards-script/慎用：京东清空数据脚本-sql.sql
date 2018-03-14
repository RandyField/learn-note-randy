  update TRP_AwardReceive set OpenId=null,SubmitTime=null,ReceiveTime=null,Phone=null where OpenId is not null and  ActivityId='67'
  or ActivityId='70' or ActivityId='69' or ActivityId='70' or ActivityId='71' or ActivityId='72'

  delete  from TRP_ScanCount where ActivityId='67'
  or ActivityId='70' or ActivityId='69' or ActivityId='70' or ActivityId='71' or ActivityId='72'


    delete  from TRP_OpenCount where ActivityId='67'
  or ActivityId='70' or ActivityId='69' or ActivityId='70' or ActivityId='71' or ActivityId='72'
