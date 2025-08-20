CONVERSATION_HISTORY_SESSION_STATE = 'conversation_history'

import gettext
_gettext = gettext.gettext

SENTIMENTS_SESSION_STATE = 'Sentiments'
AUTHENTICATION_SESSION_STATE = 'authentication_status'
USER_TEXT_SESSION_STATE = 'user_input'

# English Sentiments (GPT-3.5)
Sentiments_GPT = {
    "Hotel_feedback.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        This analysis provides a comprehensive sentiment overview, breaking down the customer feedback into 
        <strong>praises & concerns</strong> from customers.
    </p>
    <p style="font-size: 16px;">
        The sentiment analysis of the customer feedback reveals a 
        <strong>mixed sentiment</strong>.
    </p>
</div>

- Concerns: 
    - Dissatisfaction with cleanliness and customer service.
    - Reports of dirty rooms and bugs.
- Praises: 
    - Location
    - Staff
    - Amenities
    - Friendly staff, good breakfast, and convenient location.
    """),

    "POS_System.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        This analysis provides a comprehensive sentiment overview, breaking down the customer feedback into 
        <strong>praises & concerns</strong> from customers.
    </p>
    <p style="font-size: 16px;">
        The sentiment analysis of the customer feedback reveals a 
        <strong>mixed sentiment</strong>.
    </p>
</div>

- Positive Points: 
    - User-friendly interface
    - Seamless inventory tracking
    - Helpful features
- Issues: 
    - System crashes
    - Poor regional language support
    - Digital payment integration failures
    """)
}

# English Sentiments (Llama2)
Sentiments_Llama3 = {
    "Hotel_feedback.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        This analysis provides a comprehensive sentiment overview, breaking down the customer feedback into 
        <strong>praises & concerns</strong> from customers.
    </p>
    <p style="font-size: 16px;">
        The sentiment analysis of the customer feedback reveals a 
        <strong>positively skewed sentiment</strong>, with around 60% of the reviews being positive, 20% neutral, and 20% negative.
    </p>
</div>

- Positive Points: 
    - Cleanliness of the room and hotel (Reviews 7, 10, 11, 12, 15)
    - Friendly and helpful staff (Reviews 7, 10, 11, 13, 14, 15)
    - Good location (Reviews 7, 8, 10, 11, 14, 15)
    - Delicious breakfast (Reviews 7, 10, 11, 15)
    - Comfortable and spacious rooms (Reviews 7, 10, 11, 12, 15)
- Issues: 
    - Dirty rooms and poor housekeeping (Reviews 1, 2, 3)
    - Poor customer service (Review 3)
    - Limited amenities (Review 9)
    - No free breakfast (Review 13)
    """),

    "POS_System.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        This analysis provides a comprehensive sentiment overview, breaking down the customer feedback into 
        <strong>praises & concerns</strong> from customers.
    </p>
    <p style="font-size: 16px;">
        The sentiment analysis of the customer feedback reveals a 
        <strong>mixed sentiment</strong>, with a slight leaning towards being negative.
    </p>
</div>

- Positive Points: 
    - User-friendly interface (mentioned by 2 customers)
    - GST integration (mentioned by 1 customer)
    - Seamless inventory tracking feature (mentioned by 1 customer)
    - Regional language support (mentioned by 1 customer)
    - Cloud backup (mentioned by 1 customer)
    - Analytical features (mentioned by 1 customer)
    - Real-time features for faster payment systems (mentioned by 1 customer)
- Issues: 
    - Glitches and crashes (mentioned by 3 customers)
    - Slow performance (mentioned by 2 customers)
    - Poor customer support (mentioned by 2 customers)
    - Difficulty in integrating with existing CRM (mentioned by 1 customer)
    - Limited training materials (mentioned by 1 customer)
    - Digital payment integration issues (mentioned by 1 customer)
    - Language support issues (mentioned by 1 customer)
    - Limited features compared to competitors (mentioned by 1 customer)
    """)
}

# Japanese Sentiments (GPT-3.5)
japanese_sentiments_GPT = {
    "Hotel_feedback.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        この分析では、顧客からのフィードバックを賞賛と懸念に分類して、包括的なセンチメントの概要を提供します。
    </p>
    <p style="font-size: 16px;">
        顧客フィードバックのセンチメント分析により、さまざまなセンチメントが明らかになりました。
    </p>
</div>

- 懸念事項: 
    - 清潔感や接客に不満。
    - 汚部屋やバグの報告。
- 賞賛: 
    - 位置
    - スタッフ
    - アメニティ
    - フレンドリーなスタッフ、おいしい朝食、便利なロケーション。
    """),

    "POS_System.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        この分析では、顧客からのフィードバックを賞賛と懸念に分類して、包括的なセンチメントの概要を提供します。
    </p>
    <p style="font-size: 16px;">
        顧客フィードバックのセンチメント分析により、さまざまなセンチメントが明らかになりました。
    </p>
</div>

- 良い点: 
    - ユーザーフレンドリーなインターフェース
    - シームレスな在庫追跡
    - 便利な機能
- 問題: 
    - システムクラッシュ
    - 地域言語のサポートが不十分
    - デジタル決済統合の失敗
    """)
}

# Japanese Sentiments (Llama2)
japanese_sentiments_Llama3 = {
    "Hotel_feedback.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        この分析では、顧客からのフィードバックを賞賛と懸念に分類して、包括的なセンチメントの概要を提供します。
    </p>
    <p style="font-size: 16px;">
        顧客フィードバックのセンチメント分析により、約60％のレビューがポジティブ、20％が中立、20％がネガティブであることがわかりました。
    </p>
</div>

- 賞賛: 
    - 部屋とホテルの清潔さ (レビュー 7, 10, 11, 12, 15)
    - 親切でフレンドリーなスタッフ (レビュー 7, 10, 11, 13, 14, 15)
    - 良い立地 (レビュー 7, 8, 10, 11, 14, 15)
    - 美味しい朝食 (レビュー 7, 10, 11, 15)
    - 快適で広々とした部屋 (レビュー 7, 10, 11, 12, 15)
- 懸念: 
    - 汚れた部屋と悪いハウスキーピング (レビュー 1, 2, 3)
    - 悪いカスタマーサービス (レビュー 3)
    - 限られたアメニティ (レビュー 9)
    - 無料朝食なし (レビュー 13)
    """),

    "POS_System.pdf": _gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        この分析では、顧客からのフィードバックを賞賛と懸念に分類して、包括的なセンチメントの概要を提供します。
    </p>
    <p style="font-size: 16px;">
        顧客フィードバックのセンチメント分析により、ネガティブな傾向が若干ある<strong>混合センチメント</strong>が明らかになりました。
    </p>
</div>

- 賞賛:
    - ユーザーフレンドリーなインターフェース (2人の顧客が言及)
    - GST統合 (1人の顧客が言及)
    - シームレスな在庫追跡機能 (1人の顧客が言及)
    - 地域言語サポート (1人の顧客が言及)
    - クラウドバックアップ (1人の顧客が言及)
    - 分析機能 (1人の顧客が言及)
    - リアルタイム機能による迅速な決済システム (1人の顧客が言及)
- 懸念:
    - グリッチとクラッシュ (3人の顧客が言及)
    - 遅いパフォーマンス (2人の顧客が言及)
    - 低品質のカスタマーサポート (2人の顧客が言及)
    - 既存のCRMとの統合の難しさ (1人の顧客が言及)
    - 限られたトレーニング教材 (1人の顧客が言及)
    - デジタル決済統合の問題 (1人の顧客が言及)
    - 言語サポートの問題 (1人の顧客が言及)
    - 競合他社に比べて限られた機能 (1人の顧客が言及)
    """)
}

# English Insights (GPT-3.5)
insights_GPT = {
    "Hotel_feedback.pdf": """
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        The analysis highlights key areas of satisfaction and concern, enabling you to focus your efforts on areas that need improvement based on identified KPIs.
    </p>
    <p style="font-size: 16px;">
        Based on the feedback, here are the <strong>actionable insights and observations</strong>:
    </p>
</div>

###### Cleanliness:
- Observations: Dirty floors, unclean bathrooms, bugs.
- Action: Prioritize improving cleanliness.
- KPI: Increase in positive reviews regarding cleanliness.

###### Customer Service:
- Observations: Reports of poor service and unhelpful staff.
- Action: Enhance training and monitoring.
- KPI: More positive feedback about service quality.

###### Breakfast Quality:
- Observations: Mixed reviews on breakfast offerings.
- Action: Add more variety, improve quality.
- KPI: Improved feedback on breakfast.

###### Room Comfort:
- Observations: Diverse experiences with room quality.
- Action: Maintain cleanliness and update amenities.
- KPI: Enhanced feedback on room comfort and maintenance.

###### Location:
- Observations: High praise for location.
- Action: Highlight location in promotions.
- KPI: Continued positive mentions of location.

###### Value for Money:
- Observations: Varied views on value proposition.
- Action: Ensure value matches pricing.
- KPI: Improved perception of value for money.
""",
    "POS_System.pdf": """
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        The analysis highlights key areas of satisfaction and concern, enabling you to focus your efforts on areas that need improvement based on identified KPIs.
    </p>
    <p style="font-size: 16px;">
        Based on the feedback, here are the <strong>actionable insights and observations</strong>:
    </p>
</div>

###### User Interface:
- Observations: Highly user-friendly interface.
- KPI: User Satisfaction Score (USS) or UX metrics.

###### GST Integration:
- Observations: Made invoicing more efficient.
- KPI: Accuracy and efficiency of invoicing.

###### Inventory Tracking:
- Observations: Positive feedback from boutique owners.
- KPI: High Inventory Accuracy.

###### Payment Integration:
- Observations: Quick checkouts but some integration issues.
- KPI: Average Transaction Time.

###### Regional Language Support:
- Observations: Valuable for diverse staff.
- KPI: Language Support Satisfaction Score.

###### System Stability:
- Observations: Some reports of crashes and lags.
- KPI: System Uptime.
"""
}

# English Insights (Llama2)
insights_Llama3 = {
    "Hotel_feedback.pdf": """
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        The analysis highlights key areas of satisfaction and concern, enabling you to focus your efforts on areas that need improvement based on identified KPIs.
    </p>
    <p style="font-size: 16px;">
        Based on the feedback, here are the <strong>actionable insights and observations</strong>:
    </p>
</div>

###### Cleanliness:
- Observations: Dirty rooms, floors, and bathrooms.
- KPI: Cleanliness rating (e.g., 80% or higher)
- Recommended Action: Implement a rigorous cleaning schedule, including daily inspections and regular deep cleaning of rooms and public areas. Provide additional training to housekeeping staff to ensure they are equipped to maintain high cleanliness standards.

###### Location:
- Observations: High praise for central location.
- KPI: Customer satisfaction with location (e.g., 90% or higher)
- Recommended Action: Continue to highlight the hotel's central location in marketing materials and provide customers with information on nearby attractions and amenities.

###### Customer Service:
- Observations: Mixed reviews on service quality.
- KPI: Customer satisfaction with service (e.g., 85% or higher)
- Recommended Action: Provide additional training to all staff members on customer service, including conflict resolution and communication skills. Implement a system for tracking customer feedback and addressing concerns promptly.

###### Breakfast:
- Observations: Positive feedback on variety and quality.
- KPI: Customer satisfaction with breakfast (e.g., 85% or higher)
- Recommended Action: Continue to offer a wide variety of breakfast options, including hot and cold dishes, and consider adding new options to keep the menu fresh. Ensure that breakfast staff are friendly and attentive to customer needs.

###### Pest Control:
- Observations: Reports of pests (bugs) in rooms.
- KPI: Pest control rating (e.g., 95% or higher)
- Recommended Action: Conduct a thorough investigation into the pest control issues and implement a comprehensive plan to prevent future occurrences. This may include hiring a pest control service, conducting regular inspections, and providing additional training to housekeeping staff.

###### Room Quality:
- Observations: Issues with amenities and maintenance.
- KPI: Room quality rating (e.g., 80% or higher)
- Recommended Action: Conduct a thorough inspection of all rooms and address any maintenance or amenity issues promptly. Consider adding amenities such as a mini-bar or in-room coffee maker to enhance the customer experience.
""",

    "POS_System.pdf": """
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        The analysis highlights key areas of satisfaction and concern, enabling you to focus your efforts on areas that need improvement based on identified KPIs.
    </p>
    <p style="font-size: 16px;">
        Based on the feedback, here are the <strong>actionable insights and observations</strong>:
    </p>
</div>

###### Customer Satisfaction:
- Observations: Mixed reviews about the POS system, with praise for its user-friendly interface and criticism for crashes and poor support.
- KPI: Customer satisfaction rating
- Recommended Action: Conduct regular surveys to measure satisfaction and provide additional training resources and support.

###### User Experience:
- Observations: Positive feedback on the interface but concerns about performance during updates.
- KPI: User experience metrics
- Recommended Action: Conduct usability testing and optimize the interface for better performance. Implement a robust update mechanism.

###### Inventory Management:
- Observations: The inventory tracking feature is highly valued, especially in retail.
- KPI: Inventory management accuracy
- Recommended Action: Develop more advanced features like real-time tracking and automated re-ordering.

###### Digital Payments:
- Observations: Significant feature for many customers but has integration issues.
- KPI: Digital payment success rate
- Recommended Action: Enhance digital payment integration to include more options like mobile wallets and UPI.

###### Regional Language Support:
- Observations: Critical feature but has implementation issues.
- KPI: Language support satisfaction score
- Recommended Action: Review and improve the regional language support feature and add more options.

###### Customer Support:
- Observations: Mixed experiences with customer support.
- KPI: Customer support satisfaction score
- Recommended Action: Implement a robust support system with multiple channels and train staff to address concerns promptly.
"""
}

# Japanese Insights (GPT-3.5)
japanese_insights_GPT = {
   "Hotel_feedback.pdf" :_gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        分析により、満足度と懸念の主要な領域が強調表示され、特定された KPI に基づいて改善が必要な領域に重点的に取り組むことができます。
    </p>
    <p style="font-size: 16px;">
        フィードバックに基づいて、<strong>実用的な洞察と観察</strong>を以下に示します。
    </p>
</div>

###### 清潔さ:
- 所見: 汚れた床、不潔なバスルーム、虫。
- アクション: 清潔さを改善することを優先します。
- KPI: 清潔さに関する肯定的なレビューの増加。

###### 顧客サービス:
- 所見: サービスが悪く、スタッフが役に立たないという報告。
- アクション: トレーニングとモニタリングを強化します。
- KPI: サービス品質に関するより肯定的なフィードバック。

###### 朝食の質:
- 所見: 朝食の提供についてはさまざまなレビューがあります。
- アクション: 多様性を追加し、品質を向上させます。
- KPI: 朝食に関するフィードバックの改善。

###### 部屋の快適さ:
- 所見: 部屋の品質に関する多様な体験。
- アクション: 清潔さを維持し、設備を更新します。
- KPI: 部屋の快適さとメンテナンスに関するフィードバックの強化。

###### 位置:
- 所見：立地に関しては高評価。
- アクション: プロモーションで場所を強調表示します。
- KPI: 立地についてポジティブな言及を続ける。

###### コストパフォーマンス:
- 所見: 価値提案に関するさまざまな見解。
- アクション: 値が価格設定と一致していることを確認してください。
- KPI: 金額に見合った価値に対する認識の向上。
"""),
   "POS_System.pdf" :_gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        分析により、満足度と懸念の主要な領域が強調表示され、特定された KPI に基づいて改善が必要な領域に重点的に取り組むことができます。
    </p>
    <p style="font-size: 16px;">
        フィードバックに基づいて、<strong>実用的な洞察と観察</strong>を以下に示します。
    </p>
</div>

###### ユーザーインターフェース:
- 所見: 非常にユーザーフレンドリーなインターフェース。
- KPI: ユーザー満足度スコア (USS) または UX 指標。

###### GST の統合:
- 所見: 請求書の発行がより効率的になりました。
- KPI: 請求書の正確さと効率。

###### 在庫追跡:
- 所見: ブティックのオーナーからの肯定的なフィードバック。
- KPI: 高い在庫精度。

###### 支払いの統合:
- 所見: チェックアウトは迅速ですが、統合に問題がいくつかあります。
- KPI: 平均トランザクション時間。

###### 地域言語のサポート:
- 所見: 多様なスタッフにとって貴重。
- KPI: 言語サポート満足度スコア。

###### システムの安定性:
- 所見: クラッシュと遅延に関するいくつかの報告。
- KPI: システム稼働時間。
""")
}

# Japanese Insights (Llama2)
japanese_insights_Llama3 = {
   "Hotel_feedback.pdf" :_gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        分析により、満足度と懸念の主要な領域が強調表示され、特定された KPI に基づいて改善が必要な領域に重点的に取り組むことができます。
    </p>
    <p style="font-size: 16px;">
        フィードバックに基づいて、<strong>実用的な洞察と観察</strong>を以下に示します。
    </p>
</div>

###### 清潔さ:
- 所見: 汚れた部屋、床、バスルーム。
- KPI: 清潔さの評価 (例：80％以上)
- 推奨アクション: 厳格な清掃スケジュールを実施し、日常点検および定期的な徹底清掃を行います。清掃スタッフに追加のトレーニングを提供し、高い清潔基準を維持できるようにします。

###### 立地:
- 所見: 中心部の立地に対する高評価。
- KPI: 立地に対する顧客満足度 (例：90％以上)
- 推奨アクション: マーケティング資料でホテルの中心部の立地を強調し、近隣の観光地やアメニティに関する情報を顧客に提供します。

###### カスタマーサービス:
- 所見: サービスの質に関する賛否両論。
- KPI: サービスに対する顧客満足度 (例：85％以上)
- 推奨アクション: 全スタッフに追加のカスタマーサービストレーニングを提供し、コンフリクト解決およびコミュニケーションスキルを向上させます。顧客フィードバックを追跡し、懸念事項に迅速に対応するシステムを導入します。

###### 朝食:
- 所見: バラエティと質に対するポジティブなフィードバック。
- KPI: 朝食に対する顧客満足度 (例：85％以上)
- 推奨アクション: 温かい料理と冷たい料理を含む幅広い朝食オプションを提供し、新しいオプションを追加してメニューを新鮮に保つことを検討します。朝食スタッフが顧客のニーズにフレンドリーで注意深いことを確認します。

###### 害虫駆除:
- 所見: 部屋に害虫（虫）がいるという報告。
- KPI: 害虫駆除の評価 (例：95％以上)
- 推奨アクション: 害虫駆除の問題を徹底的に調査し、将来的な発生を防ぐための包括的な計画を実施します。害虫駆除サービスを雇い、定期的な検査を行い、清掃スタッフに追加のトレーニングを提供します。

###### 部屋の品質:
- 所見: アメニティとメンテナンスの問題。
- KPI: 部屋の品質評価 (例：80％以上)
- 推奨アクション: 全ての部屋の徹底的な点検を行い、メンテナンスやアメニティの問題に迅速に対応します。ミニバーや客室内のコーヒーメーカーなどのアメニティを追加して顧客体験を向上させることを検討します。
"""),

   "POS_System.pdf" :_gettext("""
<div style="font-family: 'Arial', sans-serif; text-align: left;">
    <p style="font-size: 16px;">
        分析により、満足度と懸念の主要な領域が強調表示され、特定された KPI に基づいて改善が必要な領域に重点的に取り組むことができます。
    </p>
    <p style="font-size: 16px;">
        フィードバックに基づいて、<strong>実用的な洞察と観察</strong>を以下に示します。
    </p>
</div>

###### 顧客満足度:
- 所見: POSシステムに関するレビューは賛否両論であり、ユーザーフレンドリーなインターフェースを賞賛する声がある一方、クラッシュやサポートの質に関する批判もあります。
- KPI: 顧客満足度評価
- 推奨アクション: 満足度を測定し、改善点を特定するために定期的な調査を実施します。追加のトレーニングリソースとサポートを提供します。

###### ユーザー体験:
- 所見: インターフェースに対するポジティブなフィードバックがある一方、アップデート時のパフォーマンスに関する懸念もあります。
- KPI: ユーザー体験指標
- 推奨アクション: ユーザビリティテストを実施し、インターフェースのパフォーマンスを最適化します。システムダウンタイムを最小限に抑えるために、堅牢なアップデートメカニズムを実装します。

###### 在庫管理:
- 所見: 在庫追跡機能は特に小売業界で高く評価されています。
- KPI: 在庫管理の精度
- 推奨アクション: リアルタイム追跡や自動再注文などの高度な機能を開発し、顧客体験をさらに向上させます。

###### デジタル決済:
- 所見: 多くの顧客にとって重要な機能ですが、統合に問題があります。
- KPI: デジタル決済の成功率
- 推奨アクション: モバイルウォレットやUPIなど、より多くの支払いオプションを含むようにデジタル決済統合を強化します。

###### 地域言語サポート:
- 所見: 重要な機能ですが、実装に問題があります。
- KPI: 言語サポート満足度スコア
- 推奨アクション: 地域言語サポート機能を徹底的に見直し、改善点を特定します。より多くの言語オプションを提供します。

###### カスタマーサポート:
- 所見: カスタマーサポートに関する体験は賛否両論です。
- KPI: カスタマーサポート満足度スコア
- 推奨アクション: 専用のサポートホットライン、メールサポート、オンラインチャットサポートを含む堅牢なサポートシステムを実装します。顧客サポートスタッフに包括的なトレーニングを提供し、迅速かつ効果的に顧客の懸念に対応できるようにします。
""")
}
