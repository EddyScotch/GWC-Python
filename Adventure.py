s t a r t   =   ' ' '  
  
 Y o u   w a k e   u p   o n e   m o r n i n g   a n d   f i n d   t h a t   y o u   a r e n ' t   i n   y o u r   b e d ;   y o u   a r e n ' t   e v e n   i n   y o u r   r o o m .  
  
 Y o u ' r e   i n   t h e   m i d d l e   o f   a   g i a n t   m a z e .  
  
 A   s i g n   i s   h a n g i n g   f r o m   t h e   i v y :   " Y o u   h a v e   o n e   h o u r .   D o n ' t   t o u c h   t h e   w a l l s . "  
  
  
 T h e r e   i s   a   h a l l w a y   t o   y o u r   r i g h t   a n d   t o   y o u r   l e f t .  
  
 ' ' '  
  
 p r i n t ( s t a r t )  
  
 w h i l e   t r u e :  
         p r i n t ( " T y p e   ' l e f t '   t o   g o   l e f t   o r   ' r i g h t '   t o   g o   r i g h t . " )  
  
         u s e r _ i n p u t 1 0 0   =   i n p u t ( )  
         i f   u s e r _ i n p u t 1 0 0   = =   " l e f t " :  
                 p r i n t ( " Y o u   d e c i d e   t o   g o   l e f t " )  
                 p r i n t ( " A   w i z a r d   a p p e a r s ! " )  
                 p r i n t ( " S t a y   a n d   f i g h t   o r   r u n   a w a y .   C h o o s e   ' f i g h t '   o r   ' r u n ' " )  
                 u s e r _ i n p u t 1   =   i n p u t ( )  
                 i f   u s e r _ i n p u t   = =   " f i g h t " :  
                                 p r i n t ( " T h r o w   a   ' f i r e b a l l '   o r   a   ' s n o w b a l l ' . " )  
                                 u s e r _ i n p u t 2   =   i n p u t ( )  
                                 i f   u s e r _ i n p u t 2   = =   " f i r e b a l l " :  
                                         p r i n t ( " T h e   w i z a r d   f l e e s !   Y o u   c a n   m o v e   o n . " )  
                                         p r i n t ( " G o   ' r i g h t '   o r   ' l e f t ' " )  
                                 i f   u s e r _ i n p u t 2 = =   " s n o w b a l l " :  
                                         p r i n t ( " Y o u   t h r o w   t h e   s n o w b a l l   a t   t h e   w i z a r d .   I t   a n g e r s   h i m . " )  
                                         p r i n t ( " T i m e   t o   r u n !   D o   y o u   r u n   ' q u i c k l y ' '   o r   ' s l o w l y ' ? " )  
                                         u s e r _ i n p u t 3   =   i n p u t ( )  
                                         i f   u s e r _ i n p u t 3   = =   " q u i c k l y " :  
                                                 p r i n t   ( " Y o u   o u t r u n   t h e   w i z a r d ! " )  
                                                 p r i n t   ( " Y o u   f i n d   a n   e x i t ! !   Y o u   h a v e   e s c a p e d   t h e   m a z e ,   c o n g r a t u l a t i o n s . " )  
                                         i f   u s e r _ i n p u t 3   = =   " s l o w l y " :  
                                                 p r i n t   ( " T h e   w i z a r d   p i c k s   u p   h i s   r o b e   a n d   q u i c k l y   s p r i n t s   t o w a r d s   y o u ! " )  
                                                 p r i n t ( " T h e   w i z a r d   i s   f o l l o w i n g   y o u !   D o   y o u   w a n t   t o   ' h i d e '   a g a i n s t   t h e   w a l l   o r   r u n   ' f a s t e r ' " )  
                                                 u s e r _ i n p u t 4   =   i n p u t ( )  
                                                 i f   u s e r _ i n p u t   = =   " h i d e " :  
                                                         p r i n t   ( " O h   n o   y o u   f o r g o t !   N o   t o u c h i n g   t h e   w a l l s !   G a m e   o v e r   t h e   w i z a r d   f i n d s   y o u   a n d   k i l l s   y o u " )  
                                                         c o n t i n u e  
                                                 e l i f   u s e r _ i n p u t 4   = = " f a s t e r " :  
                                                         p r i n t ( " T h e r e   i s   l i g h t   u p   a h e a d ! !   Y o u   h a v e   e s c a p e d   t h e   m a z e ,   c o n g r a t u l a t i o n s . " )  
                 i f   u s e r _ i n p u t 4   = =   " r u n " :  
                         p r i n t ( " Y o u   r u n   a w a y   a s   t h e   w i z a r d   c a c k l e s   a f t e r   y o u ! " )  
                         p r i n t ( " T h e   w i z a r d   i s   f o l l o w i n g   y o u !   D o   y o u   w a n t   t o   ' h i d e '   a g a i n s t   t h e   w a l l   o r   k e e p   ' r u n n i n g ' " )  
                         u s e r _ i n p u t 5   =   i n p u t ( )  
                         i f   u s e r _ i n p u t 5   = =   " h i d e " :  
                                 p r i n t   ( " O h   n o   y o u   f o r g o t !   N o   t o u c h i n g   t h e   w a l l s !   G a m e   o v e r ,   t h e   w i z a r d   f i n d s   y o u   a n d   k i l l s   y o u " )  
                         e l i f   u s e r _ i n p u t 5   = = " r u n n i n g " :  
                                 p r i n t ( " T h e r e   i s   l i g h t   u p   a h e a d ! !   Y o u   h a v e   e s c a p e d   t h e   m a z e ,   c o n g r a t u l a t i o n s . " )  
  
  
         e l i f   u s e r _ i n p u t 1 0 0   = =   " r i g h t " :  
                 p r i n t ( " Y o u   c h o o s e   t o   g o   r i g h t   a n d   a   g i a n t   s p i d e r   a p p e a r s ! " )  
                 p r i n t ( " T h e   s p i d e r   t r i e s   t o   b i t e   y o u   w i t h   i t s   f a n g s . . . " )  
                 p r i n t   ( " Y o u   r o l l   a w a y   j u s t   i n   t i m e ! " )  
                 p r i n t   ( " Q u i c k !   D o   y o u   ' a t t a c k '   o r   ' r u n ' ? " )  
                 u s e r _ i n p u t 6   =   i n p u t ( )  
                 i f   u s e r _ i n p u t 6   = =   " a t t a c k " :  
                         p r i n t   ( " D o   y o u   a i m   f o r   t h e   ' e y e s '   o r   t h e   ' l e g s ' ? " )  
                         u s e r _ i n p u t 7   =   i n p u t ( )  
                         i f   u s e r _ i n p u t 7   = =   " e y e s " :  
                                 p r i n t   ( " Y o u   s o c k   t h e   s p i d e r   i n   a l l   8   o f   h i s   e y e s . " )  
                                 p r i n t   ( " T h e   s p i d e r   s h a k e s   y o u   o f f   a n d   r u n s   a w a y   c r y i n g . " )  
                                 p r i n t   ( " W h i c h   w a y   d o   y o u   g o   n e x t ?   ' f o l l o w '   t h e   s p i d e r   o r   ' r e s t '   a g a i n s t   t h e   w a l l " )  
                                 u s e r _ i n p u t 8   =   i n p u t ( )  
                                 i f   u s e r _ i n p u t 8   = =   " r e s t " :  
                                         p r i n t   ( " O h   n o   y o u   f o r g o t !   N o   t o u c h i n g   t h e   w a l l s ! " )  
                                         p r i n t   ( " S p i k e s   s h o o t   o u t   o f   t h e   w a l l   k i l l i n g   y o u   i n s t a n t l y . " )  
                                 i f   u s e r _ i n p u t 8   = =   " f o l l o w " :  
                                         p r i n t   ( " Y o u   f o l l o w   t h e   t r a i l   o f   s p i d e r   t e a r s   a n d   f i n d   t h e   e x i t ! " )  
                                         p r i n t   ( " c o n g r a t u l a t i o n s !   Y o u   e s c a p e d   t h e   m a z e ! " )  
                                         u s e r _ i n p u t 9   =   i n p u t ( )  
                         i f   u s e r _ i n p u t 9   = =   " l e g s " :  
                                 p r i n t   ( " Y o u   t r y   t o   k i c k   t h e   s p i d e r ' s   l e g s ,   b u t   i t   o n l y   a n g e r s   t h e   s p i d e r . " )  
                                 p r i n t   ( " D o   y o u   k e e p   ' a t t a c k i n g '   o r   d o   y o u   g o   f o r   t h e   ' e y e s ' ? " )  
                                 u s e r _ i n p u t 1 0   =   i n p u t ( )  
                                 i f   u s e r _ i n p u t 1 0   = =   " a t t a c k i n g " :  
                                         p r i n t   ( " Y o u   c o n t i n u e   t o   k i c k   a t   t h e   s p i d e r ' s   l e g s . " )  
                                         p r i n t   ( " T h e   s p i d e r   g e t s   a n n o y e d   a n d   s q u i s h e s   y o u .   Y o u   d i e . " )  
                                 i f   u s e r _ i n p u t 1 0   = =   " e y e s " :  
                                         p r i n t   ( " Y o u   s o c k   t h e   s p i d e r   i n   a l l   8   o f   h i s   e y e s . " )  
                                         p r i n t   ( " T h e   s p i d e r   s h a k e s   y o u   o f f   a n d   r u n s   a w a y   c r y i n g . " )  
                                         p r i n t   ( " W h i c h   w a y   d o   y o u   g o   n e x t ?   ' f o l l o w '   t h e   s p i d e r   o r   ' r e s t '   a g a i n s t   t h e   w a l l " )  
                                         u s e r _ i n p u t 1 1   =   i n p u t ( )  
                                         i f   u s e r _ i n p u t 1 1   = =   " r e s t " :  
                                                 p r i n t   ( " O h   n o   y o u   f o r g o t !   N o   t o u c h i n g   t h e   w a l l s ! " )  
                                                 p r i n t   ( " S p i k e s   s h o o t   o u t   o f   t h e   w a l l   k i l l i n g   y o u   i n s t a n t l y . " )  
                                         i f   u s e r _ i n p u t 1 1   = =   " f o l l o w " :  
                                                 p r i n t   ( " Y o u   f o l l o w   t h e   t r a i l   o f   s p i d e r   t e a r s   a n d   f i n d   t h e   e x i t ! " )  
                                                 p r i n t   ( " c o n g r a t u l a t i o n s !   Y o u   e s c a p e d   t h e   m a z e ! " )  
                 u s e r _ i n p u t 1 2   =   i n p u t ( )  
                 i f   u s e r _ i n p u t 1 2   = =   " r u n " :  
                         p r i n t   ( " Y o u   q u i c k l y   r u n   a w a y   a n d   O M G   t h e r e   i s   a   s m a l l   c r a c k   i n   t h e   w a l l   w i t h   l i g h t   c o m i n g   t h r o u g h ! " )  
                         p r i n t   ( " D o   y o u   t r y   t o   ' w i d e n '   t h e   c r a c k   o r   k e e p   ' r u n n i n g ' ? " )  
                         u s e r _ i n p u t 1 3   =   i n p u t ( )  
                         i f   u s e r _ i n p u t 1 3   = =   " w i d e n " :  
                                 p r i n t   ( " Y o u   f o r g o t   y o u   c a n t   t o u c h   t h e   w a l l !   P o i s o n o u s   o o z e   s q u i r t s   o u t   o f   t h e   w a l l   a n d   y o u   d i s s o l v e   i n t o   m u s h .   G a m e   o v e r ! " )  
                         i f   u s e r _ i n p u t 1 3   = =   " r u n n i n g " :  
                                 p r i n t   ( " T h e r e   i s   a   l i g h t   a h e a d ! !   Y o u   r u n   o u t   t h e   e n d   o f   y o u r   m a z e   a n d   r e t u r n   h o m e   s a f e l y .   C o n g r a t s ! ! " )  
 