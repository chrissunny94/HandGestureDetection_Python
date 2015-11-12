package test;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.*;

import javax.swing.*;
import javax.swing.border.LineBorder;

public class PPL extends JFrame{
	private String[] options = {"Open \"Google\"", "Open VLC media Player", "Open Text Editor"
		    };
	JPanel southp=new JPanel();
	
	JPanel phold=new JPanel(new GridLayout (6,2,5,5));
	JPanel optionhold=new JPanel(new GridLayout(6,2,5,5));
	 private JComboBox box1 = new JComboBox(options);
	 
	 private JComboBox box2 = new JComboBox(options);
	 private JComboBox box3 = new JComboBox(options);
	 private JComboBox box4 = new JComboBox(options);
	 private JComboBox box5 = new JComboBox(options);
	 private JButton save=new JButton("Save");
	 private LineBorder lineborder = new LineBorder(Color.BLACK,2);
	 PPL(){
		 
		 phold.add(box1);
		 phold.add(box2);
		 phold.add(box3);
		 phold.add(box4);
		 phold.add(box5);
		 phold.add(save);
		 JLabel opt1=new JLabel("Option 1");
		 opt1.setBorder(lineborder);
		 optionhold.add( opt1);
		 optionhold.add( new JLabel("Option 2"));
		 optionhold.add( new JLabel("Option 3"));
		 optionhold.add( new JLabel("Option 4"));
		 optionhold.add( new JLabel("Option 5"));
		 optionhold.setSize(100, 200);
		 phold.setSize(300,200);
		 add(optionhold,BorderLayout.CENTER);
		 add(phold,BorderLayout.EAST);
		 add(southp,BorderLayout.SOUTH);
		 save.addActionListener(new ActionListener() {
			
			public void actionPerformed(ActionEvent e) {
				try{
				FileOutputStream output=new FileOutputStream("store.txt");
				int []preference =new int[5];
				
					preference[0]=box1.getSelectedIndex();
					preference[1]=box2.getSelectedIndex();
					preference[2]=box3.getSelectedIndex();
					preference[3]=box4.getSelectedIndex();
					preference[4]=box5.getSelectedIndex();
					for(int i=0;i<5;i++){
					output.write(preference[i]);
					}
				output.close();
				setDisplay();
				}
				catch(IOException ex){
					System.out.println(ex);
				};
				
			}
		});
	 }
		 public void setDisplay() {
			 try{
			FileInputStream input =new FileInputStream("store.txt");
			int []preference=new int [5];
			for(int i=0;i<5;i++){
				preference[i]=input.read();
				System.out.printf("%3d", preference[i]);
			}
			
			input.close();
			
			 }
			 catch(IOException ez){
				 System.out.println(ez);
			 }
			  
			  }
		 		private void display() throws IOException{
		 			BufferedInputStream input=new BufferedInputStream(new FileInputStream("store.txt"));
		 			//System.out.println(input.readLine());
		 			int r=0;
		 			String s="";
		 			while(r!=input.read()){
		 				s.concat(String.valueOf(r));
		 			}
		 			JLabel lbl=new JLabel(s);
		 			
		 			southp.add(lbl);
		 			southp.repaint();
		 			input.close();
		 			System.out.println(s);
		 		}
	 public static void main(String[] args) {
		    PPL frame = new PPL();
		    //frame.pack();
		    frame.setSize(400, 200);
		    frame.setTitle("Set User Preferences");
		    frame.setLocationRelativeTo(null); // Center the frame
		    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		    frame.setVisible(true);
		    
			    frame.setDisplay();
			    
			   
		  }
}

