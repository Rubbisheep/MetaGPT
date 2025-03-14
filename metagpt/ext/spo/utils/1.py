修改内容：
1.  spo/utils/llm_client.py   responser:    
  # For EXECUTE type, append reasoning_content if available
        try:
            response.choices[0].message.reasoning_content
            return f"Reasoning:\n{response.choices[0].message.reasoning_content}\nAnswer:\nresponse.choices[0].message.content}"
        except:
            return f"Answer:{response.choices[0].message.content}"
        # return response.choices[0].message.content